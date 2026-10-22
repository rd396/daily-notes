Python 3.13.14 (tags/v3.13.14:fd17997, Jun 10 2026, 13:03:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
greeting = "Hello"
_name = "General Kenobi."
Greeting = "There"
_bestline_ep3_ = "You are a bold one."
print(greeting + " " + Greeting + "\n\t" + _name + " " + _bestline_ep3_)
Hello There
	General Kenobi. You are a bold one.
print("{} {}\n\t{} {}".format(greeting, Greeting, _name, bestLine_ep3))
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print("{} {}\n\t{} {}".format(greeting, Greeting, _name, bestLine_ep3))
NameError: name 'bestLine_ep3' is not defined. Did you mean: '_bestline_ep3_'?
print("{} {}\n\t{} {}".format(greeting, Greeting, _name, _bestLine_ep3_))
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print("{} {}\n\t{} {}".format(greeting, Greeting, _name, _bestLine_ep3_))
NameError: name '_bestLine_ep3_' is not defined. Did you mean: '_bestline_ep3_'?
print("{} {}\n\t{} {}".format(greeting, Greeting, _name, _bestline_ep3_))
Hello There
	General Kenobi. You are a bold one.
released = 2005
# Using string concatenation:
print("Revenge of the Sith was released on May 4, " + str(released) + ".")
# Using string replacement:
print("Revenge of the Sith was released on May 4, {}.".format(released))
SyntaxError: multiple statements found while compiling a single statement
released = 2005
# Using string concatenation:
print("Revenge of the Sith was released on May 4, " + str(released) + ".")
Revenge of the Sith was released on May 4, 2005.
# Using string replacement:
print("Revenge of the Sith was released on May 4, {}.".format(released))
Revenge of the Sith was released on May 4, 2005.
a = 3
>>> b = 4
>>> c = (a ** 2 + b ** 2) ** .5
>>> print("Pythagorean Theorem: a^2 + b^2 = c^2, so when a = {} and b = {}, then c = {}".format(a, b, c))
Pythagorean Theorem: a^2 + b^2 = c^2, so when a = 3 and b = 4, then c = 5.0
>>> film = "Revenge of the Sith"
>>> print("Sith" in film)
True
>>> print("sith" in film)
False
>>> print("sith" in film.lower())
True
>>> var = "Variables are mutable"
>>> type(var)
<class 'str'>
>>> var = 3
>>> type(var)
<class 'int'>
>>> var = 3.5
>>> type(var)
<class 'float'>
>>> # If the variable contains a numeric value, it can be converted to an integer type with the int() function.
>>> var = int(var)
>>> type(var)
<class 'int'>
>>> # The variable can be converted to a string with the str() function regardless of the contents.
>>> var = str(var)
>>> type(var)
<class 'str'>
>>> # If the variable contains a numeric value, it can be converted to an float type with the float() function.
>>> var = float(var)
>>> type(var)
<class 'float'>
>>> var = True
>>> type(var)
<class 'bool'>
