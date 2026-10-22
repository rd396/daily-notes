Python 3.13.14 (tags/v3.13.14:fd17997, Jun 10 2026, 13:03:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> num = int(input("Select a positive number between 1 and 10: "))
Select a positive number between 1 and 10: 5
>>> if num > 10:
...      print("How can you expect to be the champ if you can't follow directions?")
... elif num < 1:
...       print("How can you expect to be the champ if you can't follow directions?")
... elif num < 3:
...      print("Only {} sides of beef? You need to punch more if you plan to be the champ.".format(num))
... elif num < 6:
...     print("{} sides of beef? That's a good number to punch if you want to be the champ.".format(num))
... elif num < 10:
...        print("{} sides of beef? Punching that many is a waste. Even if you become the champ, you shouldn't be wasteful.".format(num))
... else:
...     print("Well, that shouldn't have happened. {} caused an error.".format(num))
... 
...     
5 sides of beef? That's a good number to punch if you want to be the champ.
>>> awards = input("Which would you like to see, awards won or nominated?")
Which would you like to see, awards won or nominated?
>>> if awards.lower() == 'won':
...     print("Rocky won Oscars for Best Picture, Best Director, and Best Film Editing")
... elif awards.lower() == 'nominated':
...      movie = input("Which movie do you want to hear about, Rocky or Rocky III?")
...      if movie.lower() == 'rocky':
...          print("Rocky received Oscar nominations for Best Actor, Best Actress, two Best Supporting Actor, Best Original Screenplay, Best Original Song, and Best Sound.")
...      elif movie.lower() == 'rocky iii':
...          print("Rocky received Oscar an nomination for Best Original Song.")
...      else:
...          print("{} is not an acceptable entry.".format(movie))
... else:
...      print("{} is not an acceptable entry.".format(awards))
...      won
... 
...      
 is not an acceptable entry.
Traceback (most recent call last):
  File "<pyshell#27>", line 13, in <module>
    won
NameError: name 'won' is not defined
>>> reviews = 60
>>> rating = .93 if reviews > 50 else "Not enough reviews"
>>> if type(rating) == float:
...     display_rating = rating * 100
... else:
...      display_rating = rating
... print("On Rotten Tomatoes, Rocky has a rating: {} with a number of reviews: {}.".format(display_rating, reviews))
SyntaxError: invalid syntax
