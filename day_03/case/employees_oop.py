'''
    Data items we want to work with:
        1. Nature of the data: employee data
        2. Field that we are interested in: name, age, salary

    FUnctions:

        1. print the employee details
        2. update salary based on hike pct 
        3. update name 
        4. update age
'''

# --------------------------------------- Design of the class

class employee:

    # Data
    def __init__(self, n, a, s):
        self.name   = n
        self.age    = a 
        self.salary = s 

    # Functions

    def __str__(self):
        return self.name + "-" + str(self.age) + "-" + str(self.salary)

    def __repr__(self):
        return self.name

    def updateName(self, newname):
        self.name = newname

    def updateAge(self, newage):
        self.age = newage

    def calcHike(self, pct):
        self.salary = self.salary + self.salary * pct/100

    def printinfo(self):
        print("NAME             :", self.name)
        print("AGE              :", self.age)
        print("-"*40)
        print("SALARY           :", self.salary)
        #print(self )
        print("\n")

# ---------------------------------------------------------------------
# AD -> Application Developer

e1 = employee("Rajesh", 35, 1500000)
e1.calcHike(15)
e1.printinfo()
#print(e1)

e2 = employee("Anil", 36, 1600000)
e2.calcHike(16)
e2.printinfo()
#print(e2)

e3 = employee("Sunil", 37, 1700000)
e3.calcHike(17)
e3.printinfo()
#print(e3)

L = [e1, e2, e3]
for obj in L:
    obj.updateAge(obj.age + 1)
    if(obj.name == 'Anil'):
        obj.updateName(obj.name + " Kumar")
        setattr(obj, 'salary', 1345000)

for obj in L:
    obj.printinfo()


print(e1)
print(e2)
print(e3)