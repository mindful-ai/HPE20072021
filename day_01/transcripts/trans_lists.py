Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> L = [1, 2, 3, "red", "green", "blue"]
>>> E = ["Anil", 35, "HPE", "Bangalore"]
>>> 
>>> type(L)
<class 'list'>
>>> 
>>> # ----------------- subscripting
>>> 
>>> L[0]
1
>>> L[4]
'green'
>>> L[-1]
'blue'
>>> L[2:5]
[3, 'red', 'green']
>>> L[::-1]
['blue', 'green', 'red', 3, 2, 1]
>>> 
>>> # -------------------- mutability
>>> 
>>> L
[1, 2, 3, 'red', 'green', 'blue']
>>> L[-2]
'green'
>>> L[-2] = "yellow"
>>> L
[1, 2, 3, 'red', 'yellow', 'blue']
>>> 
>>> L[-1]
'blue'
>>> L[-1][2]
'u'
>>> L[-1][2] = "x"
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    L[-1][2] = "x"
TypeError: 'str' object does not support item assignment
>>> 
>>> # -------------------- operators
>>> 
>>> [1, 2, 3] + [4, 5, 6]
[1, 2, 3, 4, 5, 6]
>>> [1, 2, 3] * 3
[1, 2, 3, 1, 2, 3, 1, 2, 3]
>>> L
[1, 2, 3, 'red', 'yellow', 'blue']
>>> 2 in L
True
>>> len(L)
6
>>> isinstance(L ,list)
True
>>> type(L) is list
True
>>> del L
>>> L
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    L
NameError: name 'L' is not defined
>>> 
>>> # ------------------------ add elements
>>> 
>>> L = ["red", "green", "blue"]
>>> L.append("yellow")
>>> L
['red', 'green', 'blue', 'yellow']
>>> L.append("golden")
>>> L
['red', 'green', 'blue', 'yellow', 'golden']
>>> 
>>> L.insert(1, "orange")
>>> L
['red', 'orange', 'green', 'blue', 'yellow', 'golden']
>>> 
>>> 
>>> L1 = ["black", "grey", "white"]
>>> 
>>> L
['red', 'orange', 'green', 'blue', 'yellow', 'golden']
>>> L[2] = L1
>>> L
['red', 'orange', ['black', 'grey', 'white'], 'blue', 'yellow', 'golden']
>>> 
>>> 
>>> L = ['red', 'orange', 'green', 'blue', 'yellow', 'golden']
>>> L[2:3]
['green']
>>> L[2:3] = L1
>>> L
['red', 'orange', 'black', 'grey', 'white', 'blue', 'yellow', 'golden']
>>> 
>>> 
>>> L = ['red', 'orange', 'green', 'blue', 'yellow', 'golden']
>>> L1
['black', 'grey', 'white']
>>> L.extend(L1)
>>> L
['red', 'orange', 'green', 'blue', 'yellow', 'golden', 'black', 'grey', 'white']
>>> 
>>> 
>>> # ------------------------ removing elements
>>> 
>>> L
['red', 'orange', 'green', 'blue', 'yellow', 'golden', 'black', 'grey', 'white']
>>> 
>>> L.pop()
'white'
>>> L
['red', 'orange', 'green', 'blue', 'yellow', 'golden', 'black', 'grey']
>>> L.pop()
'grey'
>>> L.pop(1)
'orange'
>>> L
['red', 'green', 'blue', 'yellow', 'golden', 'black']
>>> 'black' in L
True
>>> L.remove('black')
>>> L
['red', 'green', 'blue', 'yellow', 'golden']
>>> 
>>> # ------------------------------ searching elements
>>> 
>>> L
['red', 'green', 'blue', 'yellow', 'golden']
>>> 'yellow' in L
True
>>> L.index('yellow')
3
>>> L.count('yellow')
1
>>> # ----------------------------- re-arranging elements
>>> 
>>> L
['red', 'green', 'blue', 'yellow', 'golden']
>>> reversed(L)
<list_reverseiterator object at 0x0000029D4C01EE48>
>>> list(reversed(L))
['golden', 'yellow', 'blue', 'green', 'red']
>>> L
['red', 'green', 'blue', 'yellow', 'golden']
>>> sorted(L)
['blue', 'golden', 'green', 'red', 'yellow']
>>> 
>>> 
>>> L.sort()
>>> L
['blue', 'golden', 'green', 'red', 'yellow']
>>> L.sort(reverse=True)
>>> L
['yellow', 'red', 'green', 'golden', 'blue']
>>> L.reverse()
>>> L
['blue', 'golden', 'green', 'red', 'yellow']
>>> L[::-1]
['yellow', 'red', 'green', 'golden', 'blue']
>>> 
>>> 
>>> # ---------------------------- iterating through the elements
>>> 
>>> for c in "abcdef":
	print(c)

	
a
b
c
d
e
f
>>> L
['blue', 'golden', 'green', 'red', 'yellow']
>>> for item in L:
	print(item)

	
blue
golden
green
red
yellow
>>> 
>>> for item in L:
	print(item.upper())

	
BLUE
GOLDEN
GREEN
RED
YELLOW
>>> for item in L[::-1]:
	print(item.upper())

	
YELLOW
RED
GREEN
GOLDEN
BLUE
>>> 
>>> # -------------------------------- copying
>>> 
>>> L
['blue', 'golden', 'green', 'red', 'yellow']
>>> L1 = L
>>> L
['blue', 'golden', 'green', 'red', 'yellow']
>>> L1
['blue', 'golden', 'green', 'red', 'yellow']
>>> L1[3] = "maroon"
>>> L1
['blue', 'golden', 'green', 'maroon', 'yellow']
>>> L
['blue', 'golden', 'green', 'maroon', 'yellow']
>>> 
>>> 
>>> import copy
>>> L2 = copy.deepcopy(L)
>>> L
['blue', 'golden', 'green', 'maroon', 'yellow']
>>> L2
['blue', 'golden', 'green', 'maroon', 'yellow']
>>> L2[2] = "white"
>>> L2
['blue', 'golden', 'white', 'maroon', 'yellow']
>>> L
['blue', 'golden', 'green', 'maroon', 'yellow']
>>> 
