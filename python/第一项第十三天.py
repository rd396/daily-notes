Python 3.13.14 (tags/v3.13.14:fd17997, Jun 10 2026, 13:03:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
motivation = "Over? Did you say 'over'? Nothing is over until we decide it is! Was it over when the Germans bombed " \
              "Pearl Harbor? Hell no! And it ain't over now. 'Cause when the goin' gets tough...the tough get goin'! " \
              "Who's with me? Let's go!"
output = ""
for letter in motivation:
     if letter.lower() in 'bcdfghjklmnpqrstvwxyz':
...           output += letter
... 
...           
>>> print(output)
vrDdysyvrNthngsvrntlwdcdtsWstvrwhnthGrmnsbmbdPrlHrbrHllnndtntvrnwCswhnthgngtstghthtghgtgnWhswthmLtsg
>>> motivation = "Over? Did you say 'over'? Nothing is over until we decide it is! Was it over when the Germans bombed " \
...              "Pearl Harbor? Hell no! And it ain't over now. 'Cause when the goin' gets tough...the tough get goin'! " \
...              "Who's with me? Let's go!"
>>> output = ""
>>> for letter in motivation:
...     if letter.lower() in 'bcdfghjklmnpqrstvwxyz':
...         continue
...     else:
...         output += letter
... 
...         
>>> print(output)
Oe? i ou a 'oe'? oi i oe ui e eie i i! a i oe e e ea oe ea ao? e o! A i ai' oe o. 'aue e e oi' e ou...e ou e oi'! o' i e? e' o!
>>> motivation = "Over? Did you say 'over'? Nothing is over until we decide it is! Was it over when the Germans bombed " \
...              "Pearl Harbor? Hell no! And it ain't over now. 'Cause when the goin' gets tough...the tough get goin'! " \
...              "Who's with me? Let's go!"
>>> output = ""
>>> for letter in motivation:
...      if letter.lower() in 'bcdfghjklmnpqrstvwxyz':
...          output += letter
...      else:
...          break
... 
...         
>>> print(output)

>>> 
>>> 
