Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # STRINGS
>>> 
\
>>> s = "python"
>>> type(s)
<class 'str'>
>>> 
>>> # ----------------------------- subscripting
>>> # s[index], s[start:end], s[start:end:skip]
>>> s
'python'
>>> s[0]
'p'

>>> s[1]
'y'
>>> s[5]
'n'
>>> s[-1]
'n'
>>> s[-2]
'o'
>>> 
>>> s[1:3]
'yt'
>>> s[1:4]
'yth'
>>> s[-5:-2]
'yth'
>>> 
>>> s[0:3]
'pyt'
>>> s[:3]
'pyt'
>>> s[3:6]
'hon'
>>> s[3:]
'hon'
>>> s[:]
'python'
>>> 
>>> s[1:5]
'ytho'
>>> s[1:5:2]
'yh'
>>> s = "computer"
>>> s[::2]
'cmue'
>>> s[::3]
'cpe'
>>> s[1::3]
'our'
>>> s[::-1]
'retupmoc'
>>> 
>>> # ----------------------------- immutable
>>> 
>>> s
'computer'
>>> s[4]
'u'
>>> s[4] = "X"
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    s[4] = "X"
TypeError: 'str' object does not support item assignment
>>> 
>>> # ------------------------------ operators
>>> 
>>> "abc" + "def"
'abcdef'
>>> "abc" * 3
'abcabcabc'
>>> 
>>> len(s)
8
>>> "put" in s
True
>>> type(s) is str
True
>>> type(s) is int
False
>>> isinstance(s, str)
True
>>> 
>>> del s
>>> s
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    s
NameError: name 's' is not defined
>>> 
>>> # --------------------------- string functions
>>> 
>>> # Case
>>> 
>>> s
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    s
NameError: name 's' is not defined
>>> s = "computer"
>>> s.upper()
'COMPUTER'
>>> s
'computer'
>>> x = s.upper()
>>> x
'COMPUTER'
>>> s
'computer'
>>> x.lower()
'computer'
>>> s.capitalize()
'Computer'
>>> 
>>> 
>>> # Checking
>>> 
>>> '1234'.isdigit()
True
>>> "123er".isdigit()
False
>>> '213sd'.isalnum()
True
>>> '23sd'.isalpha()
False
>>> 'asdf'.isalpha()
True
>>> '   '.isspace()
True
>>> 
>>> s
'computer'
>>> s.isupper()
False
>>> s.islower()
True
>>> 
>>> site = "www.google.com"
>>> site.startswith("https")
False
>>> site.endswith("com")
True
>>> 
>>> # searching
>>> 
>>> s
'computer'
>>> s.find("put")
3
>>> s.rfind("put")
3
>>> x = "mississippi"
>>> s.find("ss")
-1
>>> x.find("ss")
2
>>> x.rfind("ss")
5
>>> x.count('s')
4
>>> x.count("ss")
2
>>> 
>>> 
>>> # modifications
>>> 
>>> ip='192-29-33-1'
>>> ip.replace('-', '.')
'192.29.33.1'
>>> 
>>> amt = "16,56,344"
>>> amt = int(amt) + int(amt) * 0.15
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    amt = int(amt) + int(amt) * 0.15
ValueError: invalid literal for int() with base 10: '16,56,344'
>>> amt = int(amt.replace(',', '')) + int(amt.replace(',','')) * 0.15
>>> amt
1904795.6
>>> 
>>> ip
'192-29-33-1'
>>> newip = ip.replace('-', '.')
>>> newip
'192.29.33.1'
>>> ip
'192-29-33-1'
>>> ip = ip.replace('-', '.')
>>> ip
'192.29.33.1'
>>> # ----------------- Srividya
>>> 
>>> 
>>> s = '   456547  '
>>> int(s)
456547
>>> s.strip()
'456547'
>>> s.lstrip()
'456547  '
>>> s.rstrip()
'   456547'
>>> 
>>> 
>>> 
>>> s
'   456547  '
>>> s = "computer"
>>> s.ljust(20)
'computer            '
>>> s.rjust(20, '>')
'>>>>>>>>>>>>computer'
>>> 
>>> 
>>> text = "mary had a little lamb"
>>> text.split()
['mary', 'had', 'a', 'little', 'lamb']
>>> text.split('a')
['m', 'ry h', 'd ', ' little l', 'mb']
>>> 
>>> 
>>> L = ["python", "is", "great"]
>>> type(L)
<class 'list'>
>>> '-'.join(L)
'python-is-great'
>>> # ----------- Illayaraja
>>> 
>>> L
['python', 'is', 'great']
>>> ' '.join(L)
'python is great'
>>> 
