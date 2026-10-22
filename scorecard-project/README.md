# Home Credit 信用评分卡项目

从零构建一套可解释的信用评分卡(申请评分卡 A 卡),覆盖
**数据清洗 → WOE/IV 分箱 → 逻辑回归 → AUC/KS 评估 → 标准评分卡** 全流程。

## 目录结构

```
scorecard-project/
├── scorecard_pipeline.py     # 全流程脚本(纯 numpy/pandas/scipy)
├── REPORT.md                 # 项目报告(含结果与简历写法)
├── README.md                 # 本文件
└── outputs/
    ├── feature_iv.csv        # 85 个特征的 IV 排序
    ├── model_features.csv    # 入模的 27 个特征及系数
    ├── scorecard.csv         # 完整评分卡(每个分箱的分数)
    ├── score_distribution.csv# 评分十分位坏率分布
    └── metrics.json          # AUC / KS 等指标
```

数据目录:`../home-credit-data/`(10 个 CSV,约 2.7 GB)

## 运行

```bash
# 依赖:Python 3.10+,numpy / pandas / scipy
python scorecard_pipeline.py
```

约 50 秒跑完(30 万行 × 122 列),结果写入 `outputs/`。

## 核心结果

| 指标 | 验证集 |
|---|---|
| AUC | 0.7375 |
| KS | 0.3564 |
| 入模特征 | 27 个 |
| 评分范围 | 677 – 1115 分 |

评分十分位坏率:**24.18% → 1.53%**,单调下降,排序能力良好。

## 方法说明

- **WOE(证据权重)**:`ln(dist_good / dist_bad)`,把分箱映射成与违约风险单调相关的数值
- **IV(信息值)**:`Σ (dist_good - dist_bad) × WOE`,衡量单变量区分度
- **逻辑回归**:IRLS(牛顿法)求解,天然可解释,是评分卡行业标准
- **评分刻度**:基准 600 分 @ 好坏比 50:1,PDO=50

## 为什么不使用 scikit-learn

本项目用 `numpy` 手写 IRLS 逻辑回归与 AUC/KS 计算,
一是为了**展示对算法原理的掌握**,二是保证在任意 Python 版本上都能运行。
生产项目中可直接替换为 `sklearn.linear_model.LogisticRegression`。

## 后续可扩展

- 接入 `bureau.csv` / `previous_application.csv` 做多表特征聚合
- 对比 XGBoost / LightGBM,并用 SHAP 解释
- 加入 PSI 监控与 OOT(时间外)验证
