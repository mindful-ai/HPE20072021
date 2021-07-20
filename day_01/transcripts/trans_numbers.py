Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("Hellow HPE!")
Hellow HPE!
>>> 54 + 98
152
>>> # ----------------- NUMBERS ---------------------
>>> 
>>> a = 5
>>> b = -5.6
>>> c = 56.89
>>> type(a)
<class 'int'>
>>> type(b)
<class 'float'>
>>> type(c)
<class 'float'>
>>> 
>>> # ------------------- Operators
>>> 
>>> # Arithmetic Operators
>>> 
>>> a + b
-0.5999999999999996
>>> 
>>> a = 5
>>> b = 4
>>> c = a + b
>>> print(c)
9
>>> c
9
>>> a - b
1
>>> a * b
20
>>> a / b
1.25
>>> a % b
1
>>> a // b
1
>>> a ** b
625
>>> 
>>> # Relational Operators
>>> 
>>> a > b # Is a greater than b?
True
>>> a < b
False
>>> a >= b
True
>>> a <= b
False
>>> a == b
False
>>> a == b + 1
True
>>> a != b
True
>>> 
>>> # Logical Operators
>>> 
>>> 
>>> a > b and a == 5
True
>>> a < b and a == 5
False
>>> a < b or a == 5
True
>>> not (a < b) and a == 5
True
>>> 
>>> # ------------------------ in-built functions
>>> 
>>> a = 10
>>> b = 15
>>> a - b
-5
>>> b - a
5
>>> abs(a - b)
5
>>> a = 100
>>> type(a)
<class 'int'>
>>> hex(a)
'0x64'
>>> bin(a)
'0b1100100'
>>> oct(a)
'0o144'
>>> 
>>> s = "45"
>>> type(s)
<class 'str'>
>>> s + 10
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    s + 10
TypeError: can only concatenate str (not "int") to str
>>> int(s) + 10
55
>>> float(s) + 10
55.0
>>> 
>>> amount = "456788"
>>> amount * 0.33
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    amount * 0.33
TypeError: can't multiply sequence by non-int of type 'float'
>>> float(amount) * 0.33
150740.04
>>> 
>>> 
>>> # ------------------------ in-built modules
>>> 
>>> # module = libraries of functions and standard constants
>>> 
>>> sqrt(144)
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    sqrt(144)
NameError: name 'sqrt' is not defined
>>> import math
>>> sqrt(144)
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    sqrt(144)
NameError: name 'sqrt' is not defined
>>> math.sqrt(144)
12.0
>>> a = 45
>>> math.sin(a)
0.8509035245341184
>>> math.sin(a * 3.14/180)
0.706825181105366
>>> math.sin(a * math.pi/180)
0.7071067811865476
>>> math.sin(math.radians(45))
0.7071067811865476
>>> 
>>> import random
>>> random.randint(1, 100)
95
>>> random.randint(1, 100)
65
>>> random.randint(1, 100)
87
>>> random.randint(1, 100)
40
>>> random.randint(1, 100)
24
>>> random.randint(1, 100)
76
>>> random.randint(1, 100)
36
>>> random.randint(1, 100)
4
>>> 
