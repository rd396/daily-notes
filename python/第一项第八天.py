Python 3.13.14 (tags/v3.13.14:fd17997, Jun 10 2026, 13:03:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
theme = "East", "Bound", "Down"
type(theme)
<class 'tuple'>
print(theme)
('East', 'Bound', 'Down')
>>> good = ("Bandit", "Frog", "Snowman")
>>> type(good)
<class 'tuple'>
>>> print(good)
('Bandit', 'Frog', 'Snowman')
>>> theme[0] = "West"
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    theme[0] = "West"
TypeError: 'tuple' object does not support item assignment
>>> return_trip = "West", theme[1], theme[2]
>>> print(return_trip)
('West', 'Bound', 'Down')
>>> movie = ("Smokey and the Bandit", 1997, "Hal Needham", ("Burt Reynolds", "Sally Field", "Jerry Reed"))
>>> title, year, director, stars = movie
>>> bandit, frog, snowman = stars
>>> print("Tittle: {}\nYear: {}\nDirector: {}".format(title, year, director))
Tittle: Smokey and the Bandit
Year: 1997
Director: Hal Needham
>>> type(stars)
<class 'tuple'>
>>> print("Stars: {}\nBandit: {}\nFrog: {}\nSnowman: {}".format(stars, bandit, frog, snowman))
Stars: ('Burt Reynolds', 'Sally Field', 'Jerry Reed')
Bandit: Burt Reynolds
Frog: Sally Field
Snowman: Jerry Reed
>>> movie_list = ("Smokey and the Bandit", 1997, "Hal Needham", ["Burt Reynolds", "Sally Field", "Jerry Reed"])
>>> title, year, director, cast = movie_list
>>> type(cast)
<class 'list'>
>>> print(cast)
['Burt Reynolds', 'Sally Field', 'Jerry Reed']
>>> cast.append("Jackie Gleason")
>>> print(cast)
['Burt Reynolds', 'Sally Field', 'Jerry Reed', 'Jackie Gleason']
