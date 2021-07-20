Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = 10
>>> print("The value of a is : ", a)
The value of a is :  10
>>> print("The value of a is : ", a, " its sqare is ", a **2)
The value of a is :  10  its sqare is  100
>>> print("The value of a is %d and its square is %d" % (a, a**2))
The value of a is 10 and its square is 100
>>> 
>>> 
>>> # ---------------------- Inputs
>>> 
>>> input()
test
'test'
>>> a = input()
45
>>> a
'45'
>>> a = input("Enter a number: ")
Enter a number: 45
>>> a
'45'
>>> type(a)
<class 'str'>
>>> 
>>> a**2
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    a**2
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
>>> int(a)**2
2025
>>> 
>>> 
>>> # ------------------ Srividya
>>> 
>>> # %d -> digits
>>> # %f -> floating point number
>>> # %s -> string
>>> 
>>> a = 10
>>> b = 5.43
>>> s = "python"
>>> d = 4.555667788
>>> 
>>> print("%d %f %s %f" % (a, b, s, d))
10 5.430000 python 4.555668
>>> 
>>> # Standard format specifiers
>>> 
>>> print("%d %.2f %s %.4f" % (a, b, s, d))
10 5.43 python 4.5557
>>> 
