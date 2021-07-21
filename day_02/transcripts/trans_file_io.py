Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # FILE IO
>>> # open(), close()
>>> # read(), readline(), readlines()
>>> # write(), writelines()
>>> # seek(), tell()
>>> 
>>> 
>>> f = open(r"C:\Users\Purushotham\Desktop\hp\b2\day_02\transcripts\colors.txt", "r")
>>> f
<_io.TextIOWrapper name='C:\\Users\\Purushotham\\Desktop\\hp\\b2\\day_02\\transcripts\\colors.txt' mode='r' encoding='cp1252'>
>>> 
>>> path = "c:\next\text\data.dat"
>>> print(path)
c:
ext	ext\data.dat
>>> path = r"c:\next\text\data.dat"
>>> print(path)
c:\next\text\data.dat
>>> 
>>> 
>>> 
>>> # ------------------- reading content
>>> 
>>> c = f.read()
>>> print(c)
red
green
blue
yellow
maroon
cyan
magenta
pink
white
grey
black

>>> type(c)
<class 'str'>
>>> f.readline()
''
>>> f.tell()
75
>>> f.seek(0)
0
>>> 
>>> f.read(10)
'red\ngreen\n'
>>> f.readline()
'blue\n'
>>> f.readline()
'yellow\n'
>>> f.readline()
'maroon\n'
>>> 
>>> 
>>> f.seek(0)
0
>>> c = f.readlines()
>>> c
['red\n', 'green\n', 'blue\n', 'yellow\n', 'maroon\n', 'cyan\n', 'magenta\n', 'pink\n', 'white\n', 'grey\n', 'black\n']
>>> 
>>> # --------------------- write to a file
>>> 
>>> # -------------- Vinaya
>>> 
>>> c
['red\n', 'green\n', 'blue\n', 'yellow\n', 'maroon\n', 'cyan\n', 'magenta\n', 'pink\n', 'white\n', 'grey\n', 'black\n']
>>> c[0]
'red\n'
>>> c[0].strip()
'red'
>>> 
>>> c1 = [s.strip() for s in c]
>>> c1
['red', 'green', 'blue', 'yellow', 'maroon', 'cyan', 'magenta', 'pink', 'white', 'grey', 'black']
>>> 
>>> # ---------------------------
>>> 
>>> 
>>> f.close()
>>> f = open(r"C:\Users\Purushotham\Desktop\hp\b2\day_02\transcripts\colors2.txt", "r")
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    f = open(r"C:\Users\Purushotham\Desktop\hp\b2\day_02\transcripts\colors2.txt", "r")
FileNotFoundError: [Errno 2] No such file or directory: 'C:\\Users\\Purushotham\\Desktop\\hp\\b2\\day_02\\transcripts\\colors2.txt'
>>> f = open(r"C:\Users\Purushotham\Desktop\hp\b2\day_02\transcripts\colors2.txt", "w")
>>> f.write("COLORS REPORT\n")
14
>>> f.writelines(["color".rjust(10) + "|" + "length" + "\n", "-"*20+"\n"])
>>> f.close()
>>> c
['red\n', 'green\n', 'blue\n', 'yellow\n', 'maroon\n', 'cyan\n', 'magenta\n', 'pink\n', 'white\n', 'grey\n', 'black\n']
>>> f = open(r"C:\Users\Purushotham\Desktop\hp\b2\day_02\transcripts\colors2.txt", "a")
>>> for color in c:
	f.write(color.rjust(10) + "|" + str(len(color)) + "\n")

	
13
13
13
13
13
13
13
13
13
13
13
>>> f.close()
>>> f = open(r"C:\Users\Purushotham\Desktop\hp\b2\day_02\transcripts\colors2.txt", "a")
>>> for color in c:
	f.write(color.rjust(10) + "|" + str(len(color)) + "\n")

	
13
13
13
13
13
13
13
13
13
13
13
>>> f.close()
>>> f = open(r"C:\Users\Purushotham\Desktop\hp\b2\day_02\transcripts\colors2.txt", "a")
>>> f.write("\n\n")
2
>>> for color in c:
	f.write(color.strip().rjust(10) + "|" + str(len(color)) + "\n")

	
13
13
13
13
13
13
13
13
13
13
13
>>> f.close()
>>> 
