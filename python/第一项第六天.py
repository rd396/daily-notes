Python 3.13.14 (tags/v3.13.14:fd17997, Jun 10 2026, 13:03:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
list_1 = []
list_2 = list()
print("List 1 Type: {}\nlist 2 Type: {}".format(type(list_1), type(list_2)))
List 1 Type: <class 'list'>
list 2 Type: <class 'list'>
>>> text = "Luggage Combination"
>>> print(list(test))
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    print(list(test))
NameError: name 'test' is not defined. Did you mean: 'text'?
>>> text = "Luggage Combination"
>>> print(list(text))
['L', 'u', 'g', 'g', 'a', 'g', 'e', ' ', 'C', 'o', 'm', 'b', 'i', 'n', 'a', 't', 'i', 'o', 'n']
>>> luggage = [1, 3, 5, 2, 4]
>>> luggage.sort()
>>> print(luggage)
[1, 2, 3, 4, 5]
>>> numbers = [1, 2, 3, 4, 5]
>>> numbers_sorted = list(numbers)
>>> numbers_sorted.sort(reverse=True)
>>> print("numbers: {}\nnumbers: {}".format(numbers, numbers_sorted))
numbers: [1, 2, 3, 4, 5]
numbers: [5, 4, 3, 2, 1]
>>> numbers = [1, 2, 3, 4, 5]
>>> numbers_sorted = list(numbers)
>>> numbers_sorted.sort(reverse=True)
>>> print("numbers: {}")
numbers: {}
>>> print("numbers: {}\nnumbers_sorted: {}".format(numbers, numbers_sorted))
numbers: [1, 2, 3, 4, 5]
numbers_sorted: [5, 4, 3, 2, 1]
>>> odd = {1, 2, 3}
>>> even = [4, 5]
>>> luggage = odd + even
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    luggage = odd + even
TypeError: unsupported operand type(s) for +: 'set' and 'list'
>>> odd = [1, 3, 5]
>>> even = [2, 4]
>>> luggage = odd + even
>>> print(luggage)
[1, 3, 5, 2, 4]
>>> luggage = [1, 3, 5]
>>> even = [2, 4]
>>> luggage.extend(even)
>>> print(luggage)
[1, 3, 5, 2, 4]
>>> odd = [1, 3, 5]
>>> even = [2, 4]
>>> luggage = odd + even
>>> print("Unsorted list: {}".format(luggage))
Unsorted list: [1, 3, 5, 2, 4]
>>> print("Using the sorted() function: {}".format(sorted(luggage)))
Using the sorted() function: [1, 2, 3, 4, 5]
>>> luggage.sort()
>>> print("Using the .sort() method: {}".format(luggage))
Using the .sort() method: [1, 2, 3, 4, 5]
>>> lines = []
>>> lines.append("They told me to comb the desert, so I'm combing the desert")
>>> lines.append(YOGURT! I hate Yogurt! Even with strawberries)
SyntaxError: invalid syntax
>>> lines.append("YOGURT! I hate Yogurt! Even with strawberries")
>>> lines.append("We'll meet again in Spaceballs 2: The Quest for More Money")
>>> print(lines)
["They told me to comb the desert, so I'm combing the desert", 'YOGURT! I hate Yogurt! Even with strawberries', "We'll meet again in Spaceballs 2: The Quest for More Money"]
>>> luggage = {1, 2, 3, 4, 5}
>>> print(luggage.index(2))
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    print(luggage.index(2))
AttributeError: 'set' object has no attribute 'index'
>>> luggage = [1, 2, 3, 4, 5]
>>> print(luggage.index(2))
1
>>> quote = list("YOGURT! I hate Yogurt! Even with strawberries!")
>>> print(quote.count("t"))
4
>>> luggage = [1, 2, 3, 3, 4, 5, 6]
>>> luggage.pop()
6
>>> print(luggage)
[1, 2, 3, 3, 4, 5]
>>> luggage.pop(2)
3
>>> print(luggage)
[1, 2, 3, 4, 5]
