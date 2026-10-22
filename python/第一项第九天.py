Python 3.13.14 (tags/v3.13.14:fd17997, Jun 10 2026, 13:03:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
quotes = ["Pitter patter, let's get at 'er", "Hard no!", "H'are ya now?", "Good-n-you?", "Not so bad.", "Is that what you appreciates about me?"]
>>> quotes[0]
"Pitter patter, let's get at 'er"
>>> print(f"{quotes[2]}\n\t{quotes[3]}\n{quotes[4]}")
H'are ya now?
	Good-n-you?
Not so bad.
>>> quotes[2:5]
["H'are ya now?", 'Good-n-you?', 'Not so bad.']
>>> quotes[::2]
["Pitter patter, let's get at 'er", "H'are ya now?", 'Not so bad.']
>>> quotes[::-1]
['Is that what you appreciates about me?', 'Not so bad.', 'Good-n-you?', "H'are ya now?", 'Hard no!', "Pitter patter, let's get at 'er"]
>>> quotes[0][::2]
"Pte atr e' e t'r"
>>> quotes[0][::-1]
"re' ta teg s'tel ,rettap rettiP"
>>> wayne = "Toughest Guy in Letterkenny"
>>> wayne[::-1]
'ynnekretteL ni yuG tsehguoT'
>>> "That's a Texas sized 10-4"
"That's a Texas sized 10-4"
>>> [0:9:2]
SyntaxError: invalid syntax
>>> "That's a Texas sized 10-4"[0:9:2]
"Ta'  "
>>> quotes[:]
["Pitter patter, let's get at 'er", 'Hard no!', "H'are ya now?", 'Good-n-you?', 'Not so bad.', 'Is that what you appreciates about me?']
>>> quotes[3:]
['Good-n-you?', 'Not so bad.', 'Is that what you appreciates about me?']
>>> quotes[:3]
["Pitter patter, let's get at 'er", 'Hard no!', "H'are ya now?"]
>>> quotes[::3]
["Pitter patter, let's get at 'er", 'Good-n-you?']
>>> exchange = quotes[2:5]
>>> print(exchange)
["H'are ya now?", 'Good-n-you?', 'Not so bad.']
