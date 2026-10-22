Python 3.13.14 (tags/v3.13.14:fd17997, Jun 10 2026, 13:03:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
for i in range(1, 11):
    print("i equals {}".format(i))

    
i equals 1
i equals 2
i equals 3
i equals 4
i equals 5
i equals 6
i equals 7
i equals 8
i equals 9
i equals 10
for i in range(1, 110, 10):
    print("i equals {}".format(i))

    
i equals 1
i equals 11
i equals 21
i equals 31
i equals 41
i equals 51
i equals 61
i equals 71
i equals 81
i equals 91
i equals 101
bridge = "Stop! Who would cross the Bridge of Death must answer me these questions three, ere the other side he see."
x = 0
for letter in bridge:
    if letter in 'aeiou':
        x += 1
print("There are {} vowels in the quote.".format(x))
SyntaxError: invalid syntax
bridge = "Stop! Who would cross the Bridge of Death must answer me these questions three, ere the other side he see."
x = 0
for letter in bridge:
    if letter in 'aeiou':
        x += 1

        
print("There are {} vowels in the quote.".format(x))
There are 33 vowels in the quote.
questions = ["What is your name?", "What is your quest?", "What is the airspeed velocity of an unladen swallow?"]
for question in questions:
    print(question)

    
What is your name?
What is your quest?
What is the airspeed velocity of an unladen swallow?
print(input())



questions = ["What is your name?", "What is your quest?", "What is the airspeed velocity of an unladen swallow?"]
for question in questions:
    print(input())

    




print("=" * 26)
print("=" * 26)
for i in range(1, 13):
     for j in range(1, 13):
          print("| {:2} times {:2} equals {:3} |".format(i, j, i * j))
           print("=" * 26)
           
SyntaxError: unexpected indent
print("=" * 26)
==========================
for i in range(1, 13):
    for j in range(1, 13):
       print("| {:2} times {:2} equals {:3} |".format(i, j, i * j))

       
|  1 times  1 equals   1 |
|  1 times  2 equals   2 |
|  1 times  3 equals   3 |
|  1 times  4 equals   4 |
|  1 times  5 equals   5 |
|  1 times  6 equals   6 |
|  1 times  7 equals   7 |
|  1 times  8 equals   8 |
|  1 times  9 equals   9 |
|  1 times 10 equals  10 |
|  1 times 11 equals  11 |
|  1 times 12 equals  12 |
|  2 times  1 equals   2 |
|  2 times  2 equals   4 |
|  2 times  3 equals   6 |
|  2 times  4 equals   8 |
|  2 times  5 equals  10 |
|  2 times  6 equals  12 |
|  2 times  7 equals  14 |
|  2 times  8 equals  16 |
|  2 times  9 equals  18 |
|  2 times 10 equals  20 |
|  2 times 11 equals  22 |
|  2 times 12 equals  24 |
|  3 times  1 equals   3 |
|  3 times  2 equals   6 |
|  3 times  3 equals   9 |
|  3 times  4 equals  12 |
|  3 times  5 equals  15 |
|  3 times  6 equals  18 |
|  3 times  7 equals  21 |
|  3 times  8 equals  24 |
|  3 times  9 equals  27 |
|  3 times 10 equals  30 |
|  3 times 11 equals  33 |
|  3 times 12 equals  36 |
|  4 times  1 equals   4 |
|  4 times  2 equals   8 |
|  4 times  3 equals  12 |
|  4 times  4 equals  16 |
|  4 times  5 equals  20 |
|  4 times  6 equals  24 |
|  4 times  7 equals  28 |
|  4 times  8 equals  32 |
|  4 times  9 equals  36 |
|  4 times 10 equals  40 |
|  4 times 11 equals  44 |
|  4 times 12 equals  48 |
|  5 times  1 equals   5 |
|  5 times  2 equals  10 |
|  5 times  3 equals  15 |
|  5 times  4 equals  20 |
|  5 times  5 equals  25 |
|  5 times  6 equals  30 |
|  5 times  7 equals  35 |
|  5 times  8 equals  40 |
|  5 times  9 equals  45 |
|  5 times 10 equals  50 |
|  5 times 11 equals  55 |
|  5 times 12 equals  60 |
|  6 times  1 equals   6 |
|  6 times  2 equals  12 |
|  6 times  3 equals  18 |
|  6 times  4 equals  24 |
|  6 times  5 equals  30 |
|  6 times  6 equals  36 |
|  6 times  7 equals  42 |
|  6 times  8 equals  48 |
|  6 times  9 equals  54 |
|  6 times 10 equals  60 |
|  6 times 11 equals  66 |
|  6 times 12 equals  72 |
|  7 times  1 equals   7 |
|  7 times  2 equals  14 |
|  7 times  3 equals  21 |
|  7 times  4 equals  28 |
|  7 times  5 equals  35 |
|  7 times  6 equals  42 |
|  7 times  7 equals  49 |
|  7 times  8 equals  56 |
|  7 times  9 equals  63 |
|  7 times 10 equals  70 |
|  7 times 11 equals  77 |
|  7 times 12 equals  84 |
|  8 times  1 equals   8 |
|  8 times  2 equals  16 |
|  8 times  3 equals  24 |
|  8 times  4 equals  32 |
|  8 times  5 equals  40 |
|  8 times  6 equals  48 |
|  8 times  7 equals  56 |
|  8 times  8 equals  64 |
|  8 times  9 equals  72 |
|  8 times 10 equals  80 |
|  8 times 11 equals  88 |
|  8 times 12 equals  96 |
|  9 times  1 equals   9 |
|  9 times  2 equals  18 |
|  9 times  3 equals  27 |
|  9 times  4 equals  36 |
|  9 times  5 equals  45 |
|  9 times  6 equals  54 |
|  9 times  7 equals  63 |
|  9 times  8 equals  72 |
|  9 times  9 equals  81 |
|  9 times 10 equals  90 |
|  9 times 11 equals  99 |
|  9 times 12 equals 108 |
| 10 times  1 equals  10 |
| 10 times  2 equals  20 |
| 10 times  3 equals  30 |
| 10 times  4 equals  40 |
| 10 times  5 equals  50 |
| 10 times  6 equals  60 |
| 10 times  7 equals  70 |
| 10 times  8 equals  80 |
| 10 times  9 equals  90 |
| 10 times 10 equals 100 |
| 10 times 11 equals 110 |
| 10 times 12 equals 120 |
| 11 times  1 equals  11 |
| 11 times  2 equals  22 |
| 11 times  3 equals  33 |
| 11 times  4 equals  44 |
| 11 times  5 equals  55 |
| 11 times  6 equals  66 |
| 11 times  7 equals  77 |
| 11 times  8 equals  88 |
| 11 times  9 equals  99 |
| 11 times 10 equals 110 |
| 11 times 11 equals 121 |
| 11 times 12 equals 132 |
| 12 times  1 equals  12 |
| 12 times  2 equals  24 |
| 12 times  3 equals  36 |
| 12 times  4 equals  48 |
| 12 times  5 equals  60 |
| 12 times  6 equals  72 |
| 12 times  7 equals  84 |
| 12 times  8 equals  96 |
| 12 times  9 equals 108 |
| 12 times 10 equals 120 |
| 12 times 11 equals 132 |
| 12 times 12 equals 144 |
print("=" * 26)
==========================
i = 0
while i < 10:
 print(i)
  i += 1
  
SyntaxError: unexpected indent
i = 0
while i < 10:
    print(i)

    
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
