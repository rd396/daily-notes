Python 3.13.14 (tags/v3.13.14:fd17997, Jun 10 2026, 13:03:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> cheers = "where everybody Knows Your name."
>>> print(cheers.capitalize())
Where everybody knows your name.

>>> print(cheers.tittle())
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    print(cheers.tittle())
AttributeError: 'str' object has no attribute 'tittle'. Did you mean: 'title'?
>>> print(cheers.title())
Where Everybody Knows Your Name.
>>> print(cheers.lower())
where everybody knows your name.
>>> print(cheers.upper())
WHERE EVERYBODY KNOWS YOUR NAME.
>>> print(cheers.swapcase())
WHERE EVERYBODY kNOWS yOUR NAME.
>>> print("norm".upper())
NORM
>>> spinoff = "Frasier"
>>> yr = 1993
>>> print("The show {} was a spinoff of Cheers that first aired in {}".format(spinoff, yr))
The show Frasier was a spinoff of Cheers that first aired in 1993
>>> i = 13
>>> print("{0:2} squared is  {1:4}.".format(i, i**2))
13 squared is   169.
>>> i = 13
>>> print("{0:2} squared is  {1:<4}.".format(i, i**2))
13 squared is  169 .
>>> print("{0:2} squared is  {1:>4}.".format(i, i**2))
13 squared is   169.
>>> print("{0:2} squared is  {1:^4}.".format(i, i**2))
13 squared is  169 .
>>> msg = "END OF CODE"
>>> print("{:=^50}".format(msg))
===================END OF CODE====================
>>> print("{:.5}"format(cheers.capitalize()))
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print("{:.5}"format(cheers.capitalize()))
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print("{:.5}".format(cheers.capitalize()))
Where
>>> pi = 22 / 7
>>> print("Pi as a float is {0:f}, as a float with a precision of 2 is {0:.2f}".format(pi))
Pi as a float is 3.142857, as a float with a precision of 2 is 3.14
>>> print("The answer to life, the universe, and everything is {0:d} as an integer, or {0:=^10d} as a padded and centered integer".format(42))
The answer to life, the universe, and everything is 42 as an integer, or ====42==== as a padded and centered integer
>>> pi = 22 / 7
>>> print(f"Pi as a float is {pi:f}, as a float with a precision of 2 is {pi:.2f}")
Pi as a float is 3.142857, as a float with a precision of 2 is 3.14
>>> print(f"The answer to life, the universe, and everything is {42:d} as an integer, or {42:=^10d} as a padded and centered integer")
The answer to life, the universe, and everything is 42 as an integer, or ====42==== as a padded and centered integer
