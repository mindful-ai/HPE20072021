Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # LOOPS
>>> 
>>> 
>>> L = ["red", "green", "blue"]
>>> for item in L:
	print(item)

	
red
green
blue
>>> for item in L:
	for c in item:
		print(c.upper(), end=' ')

		
R E D G R E E N B L U E 
>>> for item in L:
	for c in item:
		print(c.upper(), end=' ')
	print()

	
R E D 
G R E E N 
B L U E 
>>> 
>>> # ------------------------ multiplication table
>>> 
>>> # 5 X 1 = 5
>>> # 5 X 2 = 10
>>> 
>>> range(10)
range(0, 10)
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(20, 30))
[20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
>>> list(range(10, 100, 5))
[10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
>>> lsit(range(100, 10, -5))
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    lsit(range(100, 10, -5))
NameError: name 'lsit' is not defined
>>> list(range(100, 10, -5))
[100, 95, 90, 85, 80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15]
>>> 
>>> 
>>> print(5, ' X ', 1, ' = ', (5*1))
5  X  1  =  5
>>> 
>>> list(range(1, 11))
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> for i in range(1, 11):
	print(5, ' X ', i, ' = ', (5*i))

	
5  X  1  =  5
5  X  2  =  10
5  X  3  =  15
5  X  4  =  20
5  X  5  =  25
5  X  6  =  30
5  X  7  =  35
5  X  8  =  40
5  X  9  =  45
5  X  10  =  50
>>> 
>>> 
>>> i = 1
>>> while i <= 10:
	print(5, ' X ', i, ' = ', (5*i))
	i = i + 1

	
5  X  1  =  5
5  X  2  =  10
5  X  3  =  15
5  X  4  =  20
5  X  5  =  25
5  X  6  =  30
5  X  7  =  35
5  X  8  =  40
5  X  9  =  45
5  X  10  =  50
>>> 
>>> # ------------------------------------- Loop controls: break, continue
>>> 
>>> for i in range(1, 11):
	print(5, ' X ', i, ' = ', (5*i))

	
5  X  1  =  5
5  X  2  =  10
5  X  3  =  15
5  X  4  =  20
5  X  5  =  25
5  X  6  =  30
5  X  7  =  35
5  X  8  =  40
5  X  9  =  45
5  X  10  =  50
>>> 
>>> for i in range(1, 11):
	if(i % 5 == 0):
		break
	print(5, ' X ', i, ' = ', (5*i))

	
5  X  1  =  5
5  X  2  =  10
5  X  3  =  15
5  X  4  =  20
>>> 
>>> for i in range(1, 11):
	if(i % 5 == 0):
		continue
	print(5, ' X ', i, ' = ', (5*i))

	
5  X  1  =  5
5  X  2  =  10
5  X  3  =  15
5  X  4  =  20
5  X  6  =  30
5  X  7  =  35
5  X  8  =  40
5  X  9  =  45
>>> 
>>> 
>>> # -------------------- Vijay
>>> 
>>> L = ["123445", "43657", "", "^%^&^&", "3245435", "546432"]
>>> for item in L:
	if(item.isdigit()):
		print(item, end= ' ')

		
123445 43657 3245435 546432 
>>> 
>>> 
>>> 
>>> for item in L:
	if item in ["", "$$$$", "&&&&"]:
		continue
	print(item, end=' ')

	
123445 43657 ^%^&^& 3245435 546432 
>>> for item in L:
	if item in ["", "$$$$", "&&&&", "^%^&^&"]:
		continue
	print(item, end=' ')

	
123445 43657 3245435 546432 
>>> 
