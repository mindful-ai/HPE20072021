Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # TUPLES
>>> 
>>> L = ["red", "green", "blue"]
>>> T = ("red", "green", "blue")
>>> 
>>> type(L)
<class 'list'>
>>> type(T)
<class 'tuple'>
>>> 
>>> L[1] = "yellow"
>>> L
['red', 'yellow', 'blue']
>>> T[1]
'green'
>>> T[1] = "yellow"
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    T[1] = "yellow"
TypeError: 'tuple' object does not support item assignment
>>> # Because the tuple is immutable
>>> # --------------------------------------------------------
>>> # You cannot add, remove, update or re-arrange elements in
>>> # place in a tuple
>>> 
>>> T
('red', 'green', 'blue')
>>> sorted(T)
['blue', 'green', 'red']
>>> T
('red', 'green', 'blue')
>>> T.sort()
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    T.sort()
AttributeError: 'tuple' object has no attribute 'sort'
>>> 
>>> list(reversed(T))
['blue', 'green', 'red']
>>> 
>>> 
>>> 
>>> # ------------------ unpacking
>>> T
('red', 'green', 'blue')
>>> r, g, b = T
>>> r
'red'
>>> g
'green'
>>> b
'blue'
>>> r, b = T
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    r, b = T
ValueError: too many values to unpack (expected 2)
>>> r, b, *x = T
>>> r
'red'
>>> b
'green'
>>> x
['blue']
>>> T
('red', 'green', 'blue')
>>> T = ('red', 'green', 'blue', "black")
>>> r, b, *x = T
>>> r
'red'
>>> b
'green'
>>> x
['blue', 'black']
>>> T = ('blue', "black", 'red', 'green', 'cyan')
>>> b1, b2, r, *x = T
>>> b1
'blue'
>>> b2
'black'
>>> r
'red'
>>> T
('blue', 'black', 'red', 'green', 'cyan')
>>> x
['green', 'cyan']
>>> # ----------------- Sandeep
>>> 
>>> # ------------- Accessing elements
>>> # subscripting
>>> T[1]
'black'
>>> T[-1]
'cyan'
>>> T[:3]
('blue', 'black', 'red')
>>> T[::-1]
('cyan', 'green', 'red', 'black', 'blue')
>>> 
>>> 
>>> # --------------- iterate
>>> 
>>> for item in T:
	print(item, end=' ')

	
blue black red green cyan 
>>> for item in T:
	print(item)

	
blue
black
red
green
cyan
>>> 
>>> # ------------------ actual scenario
>>> 
>>> d = ["raj88", "345%%$#AbcD"]
>>> # The above info can be subject to accidental changes
>>> 
>>> t = tuple(d)
>>> t
('raj88', '345%%$#AbcD')
>>> 
>>> 
>>> T
('blue', 'black', 'red', 'green', 'cyan')
>>> t
('raj88', '345%%$#AbcD')
>>> 
>>> temp = list(t)
>>> temp
['raj88', '345%%$#AbcD']
>>> temp[1] = "ABC3%^abd"
>>> temp
['raj88', 'ABC3%^abd']
>>> t = tuple(temp)
>>> t
('raj88', 'ABC3%^abd')
>>> 
