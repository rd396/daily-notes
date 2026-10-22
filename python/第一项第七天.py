Python 3.13.14 (tags/v3.13.14:fd17997, Jun 10 2026, 13:03:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> print(range(10))
range(0, 10)
>>> print(list(range(10)))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> print(range(0, 9, 2))
range(0, 9, 2)
>>> print(range(0, 9, 2) == range(0, 10, 2))
True
>>> even = range(0,10,2)
>>> odd = range(1,10,2)
>>> print("The even range is {} and the values are {}".format(even, list(even)))
The even range is range(0, 10, 2) and the values are [0, 2, 4, 6, 8]
>>> print("The odd range is {} and the values are {}".format(odd, list(odd)))
The odd range is range(1, 10, 2) and the values are [1, 3, 5, 7, 9]
>>> even = range(10,0,-2)
>>> odd = range(9,0-2)
>>> print("The even range is {} and the values are {}".format(even, list(even)))
The even range is range(10, 0, -2) and the values are [10, 8, 6, 4, 2]
>>> print("The odd range is {} and the values are {}".format(odd, list(odd)))
The odd range is range(9, -2) and the values are []
