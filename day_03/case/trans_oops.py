C:\Users\Purushotham\Desktop\hp\day_03\case>python employees_oop.py
NAME             : Rajesh
AGE              : 35
----------------------------------------
SALARY           : 1725000.0


NAME             : Anil
AGE              : 36
----------------------------------------
SALARY           : 1856000.0


NAME             : Sunil
AGE              : 37
----------------------------------------
SALARY           : 1989000.0


NAME             : Rajesh
AGE              : 36
----------------------------------------
SALARY           : 1725000.0


NAME             : Anil Kumar
AGE              : 37
----------------------------------------
SALARY           : 1345000


NAME             : Sunil
AGE              : 38
----------------------------------------
SALARY           : 1989000.0


<__main__.employee object at 0x000002918EE70780>
<__main__.employee object at 0x000002918EE707B8>
<__main__.employee object at 0x000002918EE70828>

C:\Users\Purushotham\Desktop\hp\day_03\case>python
Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> a = 19
>>> type(a)
<class 'int'>
>>> dir(a)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
>>> print(a)
19
>>> a
19
>>> from employees_oop import employee
NAME             : Rajesh
AGE              : 35
----------------------------------------
SALARY           : 1725000.0


NAME             : Anil
AGE              : 36
----------------------------------------
SALARY           : 1856000.0


NAME             : Sunil
AGE              : 37
----------------------------------------
SALARY           : 1989000.0


NAME             : Rajesh
AGE              : 36
----------------------------------------
SALARY           : 1725000.0


NAME             : Anil Kumar
AGE              : 37
----------------------------------------
SALARY           : 1345000


NAME             : Sunil
AGE              : 38
----------------------------------------
SALARY           : 1989000.0


<employees_oop.employee object at 0x000002805D418FD0>
<employees_oop.employee object at 0x000002805D4202E8>
<employees_oop.employee object at 0x000002805D420358>
>>> e = employee("Raj", 35, 3453421)
>>> print(e)
<employees_oop.employee object at 0x000002805D400438>
>>> e
<employees_oop.employee object at 0x000002805D400438>
>>> L = [e, e, e]
>>> L
[<employees_oop.employee object at 0x000002805D400438>, <employees_oop.employee object at 0x000002805D400438>, <employees_oop.employee object at 0x000002805D400438>]
>>>


--------------------------------------------------------------------------



After implementing __str__ and __repr__


>>> e = employee("Raj", 35, 4563450)
>>> print(e)
Raj-35-4563450
>>> e
Raj
>>> L = [e, e, e]
>>> L
[Raj, Raj, Raj]
>>>