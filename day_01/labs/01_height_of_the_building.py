# Program to calculate the height of the building

'''
Given/Inputs:

    distance in meters -> x
    angle in degrees   -> a

Output:

    height of the building in feet -> h

Information:

    h = tan a * x
    a -> converted to radians -> math.radians()
    h should be converted to feet -> h * 3.28
'''
import math

# input
x = float(input("Enter the distance in meters : "))
a = float(input("Enter angle in degrees       : "))

# process
h = math.tan(math.radians(a)) * (x * 3.28)

# output
print("The height of the building is %.2f feet" % h)
