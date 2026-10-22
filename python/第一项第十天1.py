Python 3.13.14 (tags/v3.13.14:fd17997, Jun 10 2026, 13:03:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> lost = True
>>> if lost:
...     print("We're going to need a montage.")
... 
...     
We're going to need a montage.
>>> lost = False
>>> if lost:
...     print("We're going to need a montage.")
... else:
...     print("Celebate by giving Adrian a kiss.")
... 
...     
Celebate by giving Adrian a kiss.
>>> prompt = input("What do you want to know? Type: 'steps' for number of steps at the Art Museum, 'bouts' for the major fights, or 'job' for Rocky's original job.")
What do you want to know? Type: 'steps' for number of steps at the Art Museum, 'bouts' for the major fights, or 'job' for Rocky's original job.
>>> if prompt.lower() == "steps":
...     print("You need to run up 72 steps to take a picture with Rocky at the Art Museum in Philadelphia.")
... elif prompt.lower() == "bouts":
...     print("Rocky (1976): Apollo Creed\nRocky II (1979): Apollo Creed\nRocky III (1982): James 'Clubber' Lang\nRocky IV (1985): Ivan Drago\nRocky V (1990): Tommy Gunn\nRocky Balboa (2006): Mason Dixon")
... elif prompt.lower() == "job":
...     print("Before becoming a professional boxer, Rocky was nothing but a 'bum' that collected payments for a loan shark.")
... else:
...     print("{} is not an acceptable entry.".format(prompt))
... 
...     
 is not an acceptable entry.
>>> steps
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    steps
NameError: name 'steps' is not defined
