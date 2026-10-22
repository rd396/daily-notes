Python 3.13.14 (tags/v3.13.14:fd17997, Jun 10 2026, 13:03:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> print("Hello"+""+"World")
HelloWorld
>>> print("Hello World")
Hello World
>>> print("Ruby"*5)
RubyRubyRubyRubyRuby
>>> print("Ew\n\tWhat do you mean 'Ew'? I don't like spam")
Ew
	What do you mean 'Ew'? I don't like spam
>>> print(1 + 1)
2
>>> print("This is the answer to life, the universe, and everything:" + 42)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print("This is the answer to life, the universe, and everything:" + 42)
TypeError: can only concatenate str (not "int") to str
>>> print("This is the answer to life, the universe, and everything: " + str(42))
This is the answer to life, the universe, and everything: 42
>>> print("The number of the {} shall be {}. No more. No less".format("counting",3))
The number of the counting shall be 3. No more. No less
>>> print(f"The number of the {'counting'} shall be {3}. No more. No less")
The number of the counting shall be 3. No more. No less
>>> print("The number of the {1} shall be {0}. No more. No less".format(3, "counting"))
The number of the counting shall be 3. No more. No less
