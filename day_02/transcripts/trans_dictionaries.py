Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> L = ["anil", 35, "HPE", "1300000", "Bangalore"]
>>> L[3]
'1300000'
>>> L[1]
35
>>> D = {"name":"anil", "age":35, "company":"HPE", "salary":"1300000", "place":"Bangalore"}
>>> D
{'name': 'anil', 'age': 35, 'company': 'HPE', 'salary': '1300000', 'place': 'Bangalore'}
>>> D["salary"]
'1300000'
>>> D["age"]
35
>>> # ----------------------------- adding, modifying and deleting
>>> 
>>> D
{'name': 'anil', 'age': 35, 'company': 'HPE', 'salary': '1300000', 'place': 'Bangalore'}
>>> D['salary']
'1300000'
>>> D['salary'] = str(float(D['salary']) + float(D['salary'])*0.15)
>>> D
{'name': 'anil', 'age': 35, 'company': 'HPE', 'salary': '1495000.0', 'place': 'Bangalore'}
>>> D['age'] = 36
>>> D
{'name': 'anil', 'age': 36, 'company': 'HPE', 'salary': '1495000.0', 'place': 'Bangalore'}
>>> 
>>> 
>>> D['country']
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    D['country']
KeyError: 'country'
>>> D['country'] = "India"
>>> D
{'name': 'anil', 'age': 36, 'company': 'HPE', 'salary': '1495000.0', 'place': 'Bangalore', 'country': 'India'}
>>> 
>>> D1 = {"addr":"J P Nagar, 6th Phase", "hobbies":["music", "movies", "magic"]}
>>> D1
{'addr': 'J P Nagar, 6th Phase', 'hobbies': ['music', 'movies', 'magic']}
>>> D.update(D1)
>>> D
{'name': 'anil', 'age': 36, 'company': 'HPE', 'salary': '1495000.0', 'place': 'Bangalore', 'country': 'India', 'addr': 'J P Nagar, 6th Phase', 'hobbies': ['music', 'movies', 'magic']}
>>> D['hobbies']
['music', 'movies', 'magic']
>>> D['hobbies'].append("sleeping")
>>> D
{'name': 'anil', 'age': 36, 'company': 'HPE', 'salary': '1495000.0', 'place': 'Bangalore', 'country': 'India', 'addr': 'J P Nagar, 6th Phase', 'hobbies': ['music', 'movies', 'magic', 'sleeping']}
>>>  D['hobbies'].insert(1, "cricket")
 
SyntaxError: unexpected indent
>>> D['hobbies'].insert(1, "cricket")
>>> D
{'name': 'anil', 'age': 36, 'company': 'HPE', 'salary': '1495000.0', 'place': 'Bangalore', 'country': 'India', 'addr': 'J P Nagar, 6th Phase', 'hobbies': ['music', 'cricket', 'movies', 'magic', 'sleeping']}
>>> 
>>> D.remove("hobbies")
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    D.remove("hobbies")
AttributeError: 'dict' object has no attribute 'remove'
>>> D.pop("hobbies")
['music', 'cricket', 'movies', 'magic', 'sleeping']
>>> D
{'name': 'anil', 'age': 36, 'company': 'HPE', 'salary': '1495000.0', 'place': 'Bangalore', 'country': 'India', 'addr': 'J P Nagar, 6th Phase'}
>>> 
>>> 
>>> # -------------- Sandeep
>>> 
>>> D
{'name': 'anil', 'age': 36, 'company': 'HPE', 'salary': '1495000.0', 'place': 'Bangalore', 'country': 'India', 'addr': 'J P Nagar, 6th Phase'}
>>> D.pop('age')
36
>>> # k -> agem v -> 36
>>> CD1 = { "age":36 }
>>> history = []
>>> history.append(CD1)
>>> 
>>> # k -> company, v -> HPE
>>> D.pop("Company")
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    D.pop("Company")
KeyError: 'Company'
>>> D.pop("company")
'HPE'
>>> history.append({"company":"HPE"})
>>> history
[{'age': 36}, {'company': 'HPE'}]
>>> D.update(history[0])
>>> D
{'name': 'anil', 'salary': '1495000.0', 'place': 'Bangalore', 'country': 'India', 'addr': 'J P Nagar, 6th Phase', 'age': 36}
>>> history
[{'age': 36}, {'company': 'HPE'}]
>>> history.pop(0)
{'age': 36}
>>> 
>>> 
>>> 
>>> D.pop("age")
36
>>> history = [{'age': 36}, {'company': 'HPE'}]
>>> 
>>> 
>>> D.update(history.pop(-1))
>>> D
{'name': 'anil', 'salary': '1495000.0', 'place': 'Bangalore', 'country': 'India', 'addr': 'J P Nagar, 6th Phase', 'company': 'HPE'}
>>> history
[{'age': 36}]
>>> 
>>> 
>>> # ---------------------- sandeep
>>> 
>>> # name  age  salary
>>> # anil   35   150K
>>> # anil   25   100K
>>> 
>>> D1 = {'name': 'anil', 'salary': '150K', 'age':35}
>>> D2 = {'name': 'anil', 'salary': '100K', 'age':25}
>>> D1
{'name': 'anil', 'salary': '150K', 'age': 35}
\
>>> D2
{'name': 'anil', 'salary': '100K', 'age': 25}
>>> MD = {'HPE01':D1, }
>>>  MD = {'HPE01':D1, 'HPE02', D2}
 
SyntaxError: unexpected indent
>>> MD = {'HPE01':D1, 'HPE02', D2}
SyntaxError: invalid syntax
>>> MD = {'HPE01':D1, 'HPE02': D2}
>>> MD
{'HPE01': {'name': 'anil', 'salary': '150K', 'age': 35}, 'HPE02': {'name': 'anil', 'salary': '100K', 'age': 25}}
>>> 
>>> D{'HPE02']['salary']
SyntaxError: invalid syntax
>>> D['HPE02']['salary']
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    D['HPE02']['salary']
KeyError: 'HPE02'
>>> MD['HPE02']['salary']
'100K'
>>> MD['HPE01']['salary']
'150K'
>>> 
>>> 
>>> # ------------------------------------- functions
>>> 
>>> D.keys()
dict_keys(['name', 'salary', 'place', 'country', 'addr', 'company'])
>>> D.value()
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    D.value()
AttributeError: 'dict' object has no attribute 'value'
>>> D.values()
dict_values(['anil', '1495000.0', 'Bangalore', 'India', 'J P Nagar, 6th Phase', 'HPE'])
>>> D.items()
dict_items([('name', 'anil'), ('salary', '1495000.0'), ('place', 'Bangalore'), ('country', 'India'), ('addr', 'J P Nagar, 6th Phase'), ('company', 'HPE')])
>>> 
>>> 

>>> # ----------------------------------------- some usage  examples
>>> 
>>> for k, v in D.items():
	print(k, ' ----> ' , v)

	
name  ---->  anil
salary  ---->  1495000.0
place  ---->  Bangalore
country  ---->  India
addr  ---->  J P Nagar, 6th Phase
company  ---->  HPE
>>> for k, v in D.items():
	print(k.rjust(10), '| ' , v)

	
      name |  anil
    salary |  1495000.0
     place |  Bangalore
   country |  India
      addr |  J P Nagar, 6th Phase
   company |  HPE
>>> MD
{'HPE01': {'name': 'anil', 'salary': '150K', 'age': 35}, 'HPE02': {'name': 'anil', 'salary': '100K', 'age': 25}}
>>> 
>>> for rec in MD.keys():
	print("-"*20)
	for k, v in MD[rec].items():
		print(k.rjust(10), '| ' , v)

		
--------------------
      name |  anil
    salary |  150K
       age |  35
--------------------
      name |  anil
    salary |  100K
       age |  25
>>> 
>>> 

>>> # --------------------- Sandeep's question re-visited
>>> # 'anil' whose salary is greater than 120K
>>> 
>>> for rec in MD.keys():
	if(MD[rec]['name'] == 'anil'):
		if(float(MD[rec]['salary'][:-1]) > 120.00):
			for k, v in MD[rec].items():
				print(k.rjust(10), '| ' , v)

				
      name |  anil
    salary |  150K
       age |  35
>>> for rec in MD.keys():
	if(MD[rec]['name'] == 'anil'):
		if(float(MD[rec]['salary'][:-1]) > 120.00):
			for k, v in MD[rec].items():
				print(k.rjust(10), '| ' , v, end=' ')

				
      name |  anil     salary |  150K        age |  35 
>>> 



>>> # -------------------- Lab session

>>> T = ({"uid":"anil45", "pswd":"ABCD234$%ab"}, {"uid":"raj87", "pswd":"BG%43434"})
>>> T
({'uid': 'anil45', 'pswd': 'ABCD234$%ab'}, {'uid': 'raj87', 'pswd': 'BG%43434'})
>>> # Add one more user into this list: user id => swe45, password => LKHG$33
#Update the password for anil45 => UYE&*^34ns
>>> 
>>> 
>>> type(T)
<class 'tuple'>
>>> D = {"uid":"swe45", "pswd": "LKHG$33"}
>>> temp = list(T)
>>> T = tuple(temp.append(D))
Traceback (most recent call last):
  File "<pyshell#133>", line 1, in <module>
    T = tuple(temp.append(D))
TypeError: 'NoneType' object is not iterable
>>> temp.append(D)
>>> temp
[{'uid': 'anil45', 'pswd': 'ABCD234$%ab'}, {'uid': 'raj87', 'pswd': 'BG%43434'}, {'uid': 'swe45', 'pswd': 'LKHG$33'}, {'uid': 'swe45', 'pswd': 'LKHG$33'}]
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> # ---
>>> 
>>> T = ({"uid":"anil45", "pswd":"ABCD234$%ab"}, {"uid":"raj87", "pswd":"BG%43434"})
>>> D = {"uid":"swe45", "pswd": "LKHG$33"}
>>> temp = list(T)
>>> temp.append(D)
>>> temp
[{'uid': 'anil45', 'pswd': 'ABCD234$%ab'}, {'uid': 'raj87', 'pswd': 'BG%43434'}, {'uid': 'swe45', 'pswd': 'LKHG$33'}]
>>> T = tuple(temp)
>>> T
({'uid': 'anil45', 'pswd': 'ABCD234$%ab'}, {'uid': 'raj87', 'pswd': 'BG%43434'}, {'uid': 'swe45', 'pswd': 'LKHG$33'})
>>> 
>>> 
>>> T[0]
{'uid': 'anil45', 'pswd': 'ABCD234$%ab'}
>>> T[0]['pswd']
'ABCD234$%ab'
>>> T[0]['pswd'] = "UYE&*^34ns"
>>> T
({'uid': 'anil45', 'pswd': 'UYE&*^34ns'}, {'uid': 'raj87', 'pswd': 'BG%43434'}, {'uid': 'swe45', 'pswd': 'LKHG$33'})
>>> 
>>> 
>>> # ------------------------ Vinaya
>>> 
>>> D
{'uid': 'swe45', 'pswd': 'LKHG$33'}
>>> 
>>> L
['anil', 35, 'HPE', '1300000', 'Bangalore']
>>> L.insert(3, "12-09-1998")
>>> L
['anil', 35, 'HPE', '12-09-1998', '1300000', 'Bangalore']
>>> 
>>> L = ['anil', 35, 'HPE', '1300000', 'Bangalore']
>>> L[3]
'1300000'
>>> int(L[3]) + float(L[3])*0.15
1495000.0
>>> # formula => int(L[3]) + float(L[3])*0.15
>>> # for data structure => ['anil', 35, 'HPE', '1300000', 'Bangalore']
>>> 
>>> 
>>> L.insert(3, "13-08-1988")
>>> int(L[3]) + float(L[3])*0.15
Traceback (most recent call last):
  File "<pyshell#175>", line 1, in <module>
    int(L[3]) + float(L[3])*0.15
ValueError: invalid literal for int() with base 10: '13-08-1988'
>>> # Program crashes
>>> 
>>> 
>>> L = ['anil', 35, 'HPE', '12091998', '1300000', 'Bangalore']
>>> int(L[3]) + float(L[3])*0.15
13905797.7
>>> # Problems in calculation
>>> 
>>> 
>>> D = {"name":"anil", "age":35, "company":"HPE", "salary":"1300000"}
>>> int(D["salary"]) + float(D["salary"])*0.15
1495000.0
>>> D["dob"] = "17-08-1988"
>>> D
{'name': 'anil', 'age': 35, 'company': 'HPE', 'salary': '1300000', 'dob': '17-08-1988'}
>>> int(D["salary"]) + float(D["salary"])*0.15
1495000.0
>>> D["dob"] = "19081988"
>>> int(D["salary"]) + float(D["salary"])*0.15
1495000.0
>>> 
>>> 
>>> a = 10
>>> type(a)
<class 'int'>
>>> b = 10.45
>>> type(b)
<class 'float'>
>>> # ------------------ Gobinda
>>> 
>>> 
