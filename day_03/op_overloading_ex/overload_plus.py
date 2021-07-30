class complex:

    '''
        2 + j5
        4 - j6
    '''

    def __init__(self, a, b):
        self.a = a
        self.b = b

    
    def __add__(self, other):     # oa + ob   ====> self + other
        return complex(self.a + other.a, self.b + other.b)

    
    def __sub__(self, other):     # oa - ob   ====> self + other
        return complex(self.a - other.a, self.b - other.b)
   
    
    
    def __str__(self):
        return str(self.a) + ' + j' +  str(self.b)
    



oa = complex(5, 12)
ob = complex(7, 8)
print(oa)
print(ob)


oc = oa + ob
print(oc)

od = oa - ob
print(od)
