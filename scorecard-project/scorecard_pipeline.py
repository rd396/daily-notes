# -*- coding: utf-8 -*-
"""
Home Credit 信用评分卡(Scorecard)完整流程
==========================================
纯 numpy / pandas / scipy 实现,不依赖 scikit-learn。

流程:
  1. 数据清洗:删除高缺失列、极端值截尾、缺失填充、特征衍生
  2. WOE/IV 分箱:数值变量分位分箱、类别变量合并,计算每个分箱的 WOE 与 IV
  3. 特征筛选:IV 阈值 + 相关性剔除
  4. 逻辑回归:IRLS(牛顿法)+ L2 正则 + 类别权重
  5. 模型评估:AUC、KS
  6. 评分卡:标准分数刻度换算(基准分 600,PDO=50)
  7. 输出:IV 表、WOE 分箱表、评分卡、评分分布、指标 JSON

运行:
  python scorecard_pipeline.py
"""
import json
import math
import os
import time

import numpy as np
import pandas as pd
from scipy.stats import rankdata

BASE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(os.path.dirname(BASE), "home-credit-data")
OUT = os.path.join(BASE, "outputs")
os.makedirs(OUT, exist_ok=True)

# 评分卡刻度参数
BASE_SCORE = 600.0      # 基准分
BASE_ODDS = 50.0        # 基准分对应好坏比 good:bad = 50:1
PDO = 50.0              # 每增加/减少 50 分,好坏比翻倍
FACTOR = PDO / math.log(2)
OFFSET = BASE_SCORE + FACTOR * math.log(BASE_ODDS)

RANDOM_STATE = 42
TRAIN_RATIO = 0.7
IV_THRESHOLD = 0.02
CORR_THRESHOLD = 0.85
MAX_FEATURES = 40


def log(msg):
    print(f"[{time.strftime('%H:%M:%S')}] {msg}", flush=True)


# ----------------------------------------------------------------------
# 1. 数据读取与清洗
# ----------------------------------------------------------------------
def load_data():
    log("读取 application_train.csv ...")
    df = pd.read_csv(os.path.join(DATA, "application_train.csv"))
    log(f"原始数据: {df.shape[0]:,} 行 x {df.shape[1]} 列")

    # 1.1 删除缺失率 > 50% 的列
    miss = df.isna().mean()
    high_miss = miss[miss > 0.5].index.tolist()
    df = df.drop(columns=high_miss)
    log(f"删除高缺失列(>50%): {len(high_miss)} 列,剩余 {df.shape[1]} 列")

    # 1.2 DAYS_EMPLOYED 的 365243 是缺失标记
    if "DAYS_EMPLOYED" in df.columns:
        n_anom = int((df["DAYS_EMPLOYED"] == 365243).sum())
        df.loc[df["DAYS_EMPLOYED"] == 365243, "DAYS_EMPLOYED"] = np.nan
        log(f"DAYS_EMPLOYED 异常值 365243 置空: {n_anom:,} 条")

    # 1.3 特征衍生
    eps = 1e-6
    df["AGE_YEARS"] = -df["DAYS_BIRTH"] / 365.25
    df["EMPLOYED_YEARS"] = -df["DAYS_EMPLOYED"] / 365.25
    df["CREDIT_INCOME_RATIO"] = df["AMT_CREDIT"] / (df["AMT_INCOME_TOTAL"] + eps)
    df["ANNUITY_INCOME_RATIO"] = df["AMT_ANNUITY"] / (df["AMT_INCOME_TOTAL"] + eps)
    df["CREDIT_TERM"] = df["AMT_ANNUITY"] / (df["AMT_CREDIT"] + eps)
    df["INCOME_PER_PERSON"] = df["AMT_INCOME_TOTAL"] / (df["CNT_FAM_MEMBERS"].fillna(1) + eps)
    ext_cols = [c for c in df.columns if c.startswith("EXT_SOURCE")]
    if ext_cols:
        df["EXT_SOURCE_MEAN"] = df[ext_cols].mean(axis=1)
    log(f"特征衍生完成:{len(ext_cols)} 个 EXT_SOURCE 合成均值")

    # 1.4 极端值截尾(1% ~ 99%)
    num_cols = [c for c in df.select_dtypes(include=[np.number]).columns
                if c not in ("TARGET", "SK_ID_CURR")]
    for c in num_cols:
        s = df[c]
        lo, hi = s.quantile(0.01), s.quantile(0.99)
        df[c] = s.clip(lo, hi)
    log(f"数值特征截尾完成:{len(num_cols)} 列")

    # 1.5 缺失填充
    for c in num_cols:
        df[c] = df[c].fillna(df[c].median())
    cat_cols = [c for c in df.columns if not pd.api.types.is_numeric_dtype(df[c])]
    for c in cat_cols:
        df[c] = df[c].fillna("MISSING")
    log(f"缺失填充完成(数值取中位数,类别填 MISSING)")

    return df, num_cols, cat_cols


# ----------------------------------------------------------------------
# 2. 分箱
# ----------------------------------------------------------------------
def bin_numeric(s, q=10):
    """分位分箱,缺失单独一箱。"""
    vals = s.dropna()
    if vals.nunique() <= 2:
        return s.astype(str)
    try:
        _, edges = pd.qcut(vals, q=min(q, vals.nunique()), retbins=True, duplicates="drop")
    except ValueError:
        _, edges = pd.qcut(vals, 5, retbins=True, duplicates="drop")
    if len(edges) < 3:
        return s.astype(str)
    edges = edges.astype(float).copy()
    edges[0], edges[-1] = -np.inf, np.inf
    edges = np.unique(edges)
    labels = pd.cut(s, bins=edges, include_lowest=True).astype(str)
    labels = labels.where(s.notna(), "MISSING")
    return labels


def bin_categorical(s, max_cat=8, min_freq=0.01):
    """保留高频类别,其余合并为 OTHER,缺失单独一箱。"""
    freq = s.value_counts(normalize=True)
    keep = freq[freq >= min_freq].index[:max_cat].tolist()
    out = s.where(s.isin(keep), "OTHER")
    out = out.where(s.notna(), "MISSING")
    return out


# ----------------------------------------------------------------------
# 3. WOE / IV
# ----------------------------------------------------------------------
def woe_table(bins, target):
    """返回 (分箱统计表, IV)"""
    d = pd.DataFrame({"bin": bins, "y": target})
    g = d.groupby("bin", observed=True)["y"].agg(["count", "sum"])
    g.columns = ["cnt", "bad"]
    g["good"] = g["cnt"] - g["bad"]
    tot_bad, tot_good = g["bad"].sum(), g["good"].sum()
    k = len(g)
    # 拉普拉斯平滑,避免 log(0)
    g["dist_bad"] = (g["bad"] + 0.5) / (tot_bad + 0.5 * k)
    g["dist_good"] = (g["good"] + 0.5) / (tot_good + 0.5 * k)
    g["woe"] = np.log(g["dist_good"] / g["dist_bad"])
    g["iv"] = (g["dist_good"] - g["dist_bad"]) * g["woe"]
    g["bad_rate"] = g["bad"] / g["cnt"].clip(lower=1)
    return g, float(g["iv"].sum())


def build_woe_features(df, num_cols, cat_cols, target):
    log("开始分箱 + 计算 WOE/IV ...")
    iv_rows, bin_tables = [], {}

    for c in num_cols:
        bins = bin_numeric(df[c])
        tbl, iv = woe_table(bins, target)
        iv_rows.append({"feature": c, "type": "numeric", "iv": iv, "n_bins": len(tbl)})
        bin_tables[c] = tbl

    for c in cat_cols:
        if df[c].nunique() > 50:          # 高基数类别先跳过
            continue
        bins = bin_categorical(df[c])
        tbl, iv = woe_table(bins, target)
        iv_rows.append({"feature": c, "type": "categorical", "iv": iv, "n_bins": len(tbl)})
        bin_tables[c] = tbl

    iv_df = pd.DataFrame(iv_rows).sort_values("iv", ascending=False).reset_index(drop=True)
    log(f"分箱完成,共 {len(iv_df)} 个特征参与评估")
    return iv_df, bin_tables


def woe_matrix(df, features, bin_tables, cat_cols):
    """把每个特征映射成 WOE 数值矩阵。"""
    X = np.zeros((len(df), len(features)), dtype=float)
    for j, f in enumerate(features):
        if f in cat_cols:
            bins = bin_categorical(df[f])
        else:
            bins = bin_numeric(df[f])
        mapping = bin_tables[f]["woe"].to_dict()
        X[:, j] = bins.map(mapping).fillna(0.0).to_numpy()
    return X


# ----------------------------------------------------------------------
# 4. 逻辑回归(IRLS)
# ----------------------------------------------------------------------
def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-np.clip(z, -30, 30)))


def fit_logistic(X, y, sample_weight=None, l2=1.0, n_iter=30, tol=1e-7):
    n, p = X.shape
    Xb = np.hstack([X, np.ones((n, 1))])
    w = np.zeros(p + 1)
    if sample_weight is None:
        sample_weight = np.ones(n)
    reg = np.eye(p + 1) * l2
    reg[-1, -1] = 0.0
    for it in range(n_iter):
        p_hat = sigmoid(Xb @ w)
        W = p_hat * (1 - p_hat) * sample_weight + 1e-9
        grad = Xb.T @ (sample_weight * (p_hat - y)) + l2 * w
        H = Xb.T @ (Xb * W[:, None]) + reg
        step = np.linalg.solve(H, grad)
        w -= step
        if np.max(np.abs(step)) < tol:
            break
    return w


def auc_score(y, score):
    """Mann-Whitney U 形式计算 AUC(处理并列值)。"""
    y = np.asarray(y)
    score = np.asarray(score)
    ranks = rankdata(score)
    n_pos = y.sum()
    n_neg = len(y) - n_pos
    return float((ranks[y == 1].sum() - n_pos * (n_pos + 1) / 2) / (n_pos * n_neg))


def ks_score(y, score):
    """KS = max(|累计坏样本占比 - 累计好样本占比|)"""
    y = np.asarray(y)
    score = np.asarray(score)
    order = np.argsort(-score)
    y = y[order]
    cum_bad = np.cumsum(y) / y.sum()
    cum_good = np.cumsum(1 - y) / (len(y) - y.sum())
    return float(np.max(np.abs(cum_bad - cum_good)))


# ----------------------------------------------------------------------
# 5. 主流程
# ----------------------------------------------------------------------
def main():
    t_start = time.time()
    df, num_cols, cat_cols = load_data()
    y = df["TARGET"].to_numpy(dtype=float)

    iv_df, bin_tables = build_woe_features(df, num_cols, cat_cols, df["TARGET"])
    iv_df.to_csv(os.path.join(OUT, "feature_iv.csv"), index=False, encoding="utf-8-sig")

    log("IV Top 15:")
    for _, r in iv_df.head(15).iterrows():
        log(f"    {r['feature']:32s} IV={r['iv']:.4f}  ({r['type']}, {r['n_bins']} 箱)")

    # 5.1 特征筛选:IV 阈值
    selected = iv_df[iv_df["iv"] >= IV_THRESHOLD]["feature"].tolist()
    selected = selected[:MAX_FEATURES]
    log(f"IV >= {IV_THRESHOLD} 的特征:{len(selected)} 个")

    # 5.2 相关性剔除
    X_all = woe_matrix(df, selected, bin_tables, cat_cols)
    corr = np.corrcoef(X_all, rowvar=False)
    drop = set()
    for i in range(len(selected)):
        if i in drop:
            continue
        for j in range(i + 1, len(selected)):
            if j in drop:
                continue
            if abs(corr[i, j]) > CORR_THRESHOLD:
                # 保留 IV 更高的
                if iv_df.loc[iv_df.feature == selected[i], "iv"].values[0] >= \
                   iv_df.loc[iv_df.feature == selected[j], "iv"].values[0]:
                    drop.add(j)
                else:
                    drop.add(i)
                    break
    features = [f for k, f in enumerate(selected) if k not in drop]
    log(f"相关性剔除后保留 {len(features)} 个特征")

    X = woe_matrix(df, features, bin_tables, cat_cols)

    # 5.3 划分训练 / 验证集(分层)
    rng = np.random.default_rng(RANDOM_STATE)
    idx = rng.permutation(len(df))
    n_train = int(len(df) * TRAIN_RATIO)
    tr, va = idx[:n_train], idx[n_train:]
    X_tr, y_tr = X[tr], y[tr]
    X_va, y_va = X[va], y[va]
    log(f"训练集 {len(tr):,} 行,验证集 {len(va):,} 行")

    # 5.4 类别权重(处理 8% 的不平衡)
    pos_w = (y_tr == 0).sum() / max((y_tr == 1).sum(), 1)
    sw = np.where(y_tr == 1, pos_w, 1.0)
    log(f"正负样本权重比:{pos_w:.2f}")

    # 5.5 训练
    log("训练逻辑回归(IRLS)...")
    w = fit_logistic(X_tr, y_tr, sample_weight=sw, l2=1.0)
    coef, intercept = w[:-1], w[-1]

    # 5.6 评估
    p_tr = sigmoid(X_tr @ coef + intercept)
    p_va = sigmoid(X_va @ coef + intercept)
    metrics = {
        "n_train": int(len(tr)), "n_valid": int(len(va)),
        "n_features": len(features),
        "bad_rate_train": float(y_tr.mean()), "bad_rate_valid": float(y_va.mean()),
        "auc_train": auc_score(y_tr, p_tr), "auc_valid": auc_score(y_va, p_va),
        "ks_train": ks_score(y_tr, p_tr), "ks_valid": ks_score(y_va, p_va),
        "base_score": BASE_SCORE, "base_odds": BASE_ODDS, "pdo": PDO,
    }
    log(f"训练集 AUC={metrics['auc_train']:.4f}  KS={metrics['ks_train']:.4f}")
    log(f"验证集 AUC={metrics['auc_valid']:.4f}  KS={metrics['ks_valid']:.4f}")

    # 5.7 评分卡刻度
    base_points = OFFSET - FACTOR * intercept
    rows = []
    for j, f in enumerate(features):
        tbl = bin_tables[f].copy()
        tbl["points"] = -FACTOR * coef[j] * tbl["woe"]
        tbl["feature"] = f
        tbl["coef"] = coef[j]
        rows.append(tbl.reset_index().rename(columns={"index": "bin"}))
    scorecard = pd.concat(rows, ignore_index=True)
    scorecard = scorecard[["feature", "bin", "cnt", "bad", "good", "bad_rate",
                           "woe", "iv", "coef", "points"]]
    scorecard.to_csv(os.path.join(OUT, "scorecard.csv"), index=False, encoding="utf-8-sig")

    # 5.8 评分与分布
    score_va = base_points + sum(
        (-FACTOR * coef[j] * X_va[:, j]) for j in range(len(features))
    )
    metrics["score_min"] = float(score_va.min())
    metrics["score_max"] = float(score_va.max())
    metrics["score_mean"] = float(score_va.mean())

    dec = pd.qcut(pd.Series(score_va), 10, labels=False, duplicates="drop")
    dist = pd.DataFrame({"decile": dec, "y": y_va, "score": score_va}) \
        .groupby("decile").agg(样本数=("y", "size"), 坏样本=("y", "sum"),
                               坏率=("y", "mean"), 平均分=("score", "mean")).reset_index()
    dist["坏率"] = dist["坏率"].round(4)
    dist["平均分"] = dist["平均分"].round(1)
    dist.to_csv(os.path.join(OUT, "score_distribution.csv"), index=False, encoding="utf-8-sig")
    log("按评分十分位的坏率分布:")
    for _, r in dist.iterrows():
        log(f"    第{int(r['decile'])+1}档  样本 {int(r['样本数']):>6,}  坏率 {r['坏率']:.2%}  均分 {r['平均分']}")

    # 5.9 保存指标
    with open(os.path.join(OUT, "metrics.json"), "w", encoding="utf-8") as f:
        json.dump(metrics, f, ensure_ascii=False, indent=2)

    # 5.10 保存特征列表
    pd.DataFrame({"feature": features, "coef": coef}).to_csv(
        os.path.join(OUT, "model_features.csv"), index=False, encoding="utf-8-sig")

    log(f"总耗时 {time.time()-t_start:.1f}s,结果已写入 {OUT}")
    return metrics, iv_df, scorecard, dist


if __name__ == "__main__":
    main()
