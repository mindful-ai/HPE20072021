Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # LAMBDA FUNCTIONS
>>> 
>>> # lambda expression
>>> # lambda <inputs> : <outputs>
>>> # lambda <inputs> : <outputs>
>>> 
>>> lambda a, b : a + b
<function <lambda> at 0x000001F08A663620>
>>> f = lambda a, b : a + b
>>> type(f)
<class 'function'>
>>> f(10, 20)
30
>>> f("abc", "def")
'abcdef'
>>> f([1,2,3], [3,4,5])
[1, 2, 3, 3, 4, 5]
>>> 
>>> f = lambda t : t * 1.8 + 32
>>> f(100)
212.0
>>> 
>>> 
>>> # --------------------- map()
>>> 
>>> T = [100, 45, 56, 88, 101]
>>> F = []
>>> for t in T:
	F.append(t * 1.8 + 32)

	
>>> F
[212.0, 113.0, 132.8, 190.4, 213.8]
>>> 
>>> F1 = map(lambda t : t * 1.8 + 32, T)
>>> F1
<map object at 0x000001F08A5F57F0>
>>> list(F1)
[212.0, 113.0, 132.8, 190.4, 213.8]
>>> 
>>> 
>>> # ------------------------------- filter()
>>> 
>>> import random
>>> RN = []
>>> for i in range(100):
	RN.append(random.randint(1, 100))

	
>>> RN
[82, 74, 90, 28, 31, 38, 31, 88, 60, 58, 99, 66, 75, 39, 5, 61, 20, 28, 36, 63, 57, 75, 36, 6, 94, 35, 39, 94, 40, 91, 85, 80, 8, 59, 12, 54, 19, 8, 42, 79, 44, 69, 24, 90, 3, 85, 27, 22, 22, 94, 17, 7, 15, 72, 7, 52, 67, 96, 19, 76, 90, 18, 72, 13, 99, 82, 18, 16, 79, 8, 66, 58, 79, 27, 31, 76, 94, 55, 4, 87, 68, 82, 91, 45, 86, 25, 45, 76, 44, 5, 69, 70, 96, 88, 97, 85, 67, 82, 29, 28]
>>> len(RN)
100
>>> RN = list(set(RN))
>>> RN
[3, 4, 5, 6, 7, 8, 12, 13, 15, 16, 17, 18, 19, 20, 22, 24, 25, 27, 28, 29, 31, 35, 36, 38, 39, 40, 42, 44, 45, 52, 54, 55, 57, 58, 59, 60, 61, 63, 66, 67, 68, 69, 70, 72, 74, 75, 76, 79, 80, 82, 85, 86, 87, 88, 90, 91, 94, 96, 97, 99]
>>> len(RN)
60
>>> 
>>> 
>>> N13 = []
>>> for n in RN:
	if(n % 13 == 0):
		N13.append(n)

		
>>> N13
[13, 39, 52, 91]
>>> 
>>> N13A = filter(lambda n : n % 13 == 0, RN)
>>> N13A
<filter object at 0x000001F08A65CBE0>
>>> list(N13A)
[13, 39, 52, 91]
>>> N13A = filter(lambda n : not n % 13 == 0, RN)
>>> N13A
<filter object at 0x000001F08A68EE10>
>>> list(N13A)
[3, 4, 5, 6, 7, 8, 12, 15, 16, 17, 18, 19, 20, 22, 24, 25, 27, 28, 29, 31, 35, 36, 38, 40, 42, 44, 45, 54, 55, 57, 58, 59, 60, 61, 63, 66, 67, 68, 69, 70, 72, 74, 75, 76, 79, 80, 82, 85, 86, 87, 88, 90, 94, 96, 97, 99]
>>> len(N13A)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    len(N13A)
TypeError: object of type 'filter' has no len()
>>> len(list(N13A))
0
>>> N13A = filter(lambda n : not n % 13 == 0, RN)
>>> len(list(N13A))
56
>>> # ----------------------------------- reduce
>>> 
>>> from functools import reduce
>>> 
>>> # import functools
>>> # functools.reduce()
>>> 
>>> L = [1,2,3,4,5]
>>> reduce(lambda a,b:a+b, L)
15
>>> # ---------------------------------------- zip
>>> 
>>> T1 = ("anil", "sunil", "raj")
>>> T2 = ("bangalore", "hyderabad", "chennai")
>>> list(zip(T1, T2))
[('anil', 'bangalore'), ('sunil', 'hyderabad'), ('raj', 'chennai')]
>>> dict(zip(T1, T2))
{'anil': 'bangalore', 'sunil': 'hyderabad', 'raj': 'chennai'}
>>> 
>>> 
>>> 
>>> c = "name,age,company,salary"
>>> r = "anil,35,hpe,1500000"
>>> 
>>> cl = c.slpit(',')
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    cl = c.slpit(',')
AttributeError: 'str' object has no attribute 'slpit'
>>> cl = c.split(',')
>>> r1 = r.split(',')
>>> c1
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    c1
NameError: name 'c1' is not defined
>>> cl
['name', 'age', 'company', 'salary']
>>> r1
['anil', '35', 'hpe', '1500000']
>>> dict(zip(cl, r1))
{'name': 'anil', 'age': '35', 'company': 'hpe', 'salary': '1500000'}
>>> 
>>> 
>>> 
>>> # ---- unuzip
>>> 
>>> D = {'name': 'anil', 'age': '35', 'company': 'hpe', 'salary': '1500000'}
>>> D.items()
dict_items([('name', 'anil'), ('age', '35'), ('company', 'hpe'), ('salary', '1500000')])
>>> w = list(zip(*D.items()))
>>> w
[('name', 'age', 'company', 'salary'), ('anil', '35', 'hpe', '1500000')]
>>> c = ','.join(w[0])
>>> r = ','.join(w[1])
>>> c
'name,age,company,salary'
>>> r
'anil,35,hpe,1500000'
>>> 
>>> 
>>> # ----------------------- comprehensions
>>> 
>>> L = list(range(1, 11))
>>> L
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> 
>>> L1 = [x**2 for x in L]
>>> L1
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
>>> L2 = [x**2 for x in L if x % 2 == 0]
>>> L2
[4, 16, 36, 64, 100]
>>> 
>>> # [], {}, ()
>>> # <expr> <loop> <condition>
>>> 
>>> S = ["red", "green", "blue", "yellow"]
>>> L
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> 
>>> 
>>> T1 = ((x, x**2, x**3) for x in L)
>>> T1
<generator object <genexpr> at 0x000001F08A64B9A8>
>>> list(T1)
[(1, 1, 1), (2, 4, 8), (3, 9, 27), (4, 16, 64), (5, 25, 125), (6, 36, 216), (7, 49, 343), (8, 64, 512), (9, 81, 729), (10, 100, 1000)]
>>> 
>>> D1 = { s:len(s) for s in S }
>>> D1
{'red': 3, 'green': 5, 'blue': 4, 'yellow': 6}
>>> 
>>> import random
>>> RN = [random.randint(1, 100) for i in range(100)]
>>> RM
Traceback (most recent call last):
  File "<pyshell#132>", line 1, in <module>
    RM
NameError: name 'RM' is not defined
>>> RN
[38, 2, 38, 11, 38, 98, 34, 93, 63, 57, 26, 79, 23, 72, 65, 48, 5, 56, 94, 82, 47, 20, 90, 100, 82, 62, 14, 68, 14, 76, 22, 96, 18, 6, 69, 74, 23, 39, 29, 76, 72, 32, 62, 30, 9, 97, 49, 37, 54, 56, 40, 70, 21, 87, 59, 36, 25, 45, 87, 32, 21, 34, 81, 52, 17, 94, 45, 58, 60, 58, 43, 88, 28, 49, 12, 82, 49, 65, 97, 90, 22, 28, 9, 46, 25, 28, 12, 44, 31, 78, 41, 78, 56, 40, 9, 26, 91, 74, 33, 28]
>>> 
>>> 
>>> # ------------------ prime numbers using comprehensions
>>> 
>>> N = 13
>>> 
>>> any([True, True, False, False])
True
>>> all([True, True, False, False])
False
>>> 
>>> [N % i == 0 for i in range(2, N)]
[False, False, False, False, False, False, False, False, False, False, False]
>>> any([N % i == 0 for i in range(2, N)])
False
>>> all([N % i != 0 for i in range(2, N)])
True
>>> N = 10
>>> all([N % i != 0 for i in range(2, N)])
False
>>> N = 17
>>> all([N % i != 0 for i in range(2, N)])
True
>>> 
>>> 
>>> # ------------------------- vinaya's question revisited
>>> 
>>> S = ["red\n", "green\n", "blue\n", "yellow\n"]
>>> S = [s.strip() for s in S]
>>> S
['red', 'green', 'blue', 'yellow']
>>> 
>>> # ---------------------------- one last thing!!
>>> 
>>> L
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> 
>>> L1 = [x**2 for x in L if x in [3, 5, 6, 9]]
>>> L1
[9, 25, 36, 81]
>>> 
>>> L2 = [x**2 if x in [3, 5, 6, 9] else x for x in L]
>>> L2
[1, 2, 9, 4, 25, 36, 7, 8, 81, 10]
>>> 
