# Program to check if the result of subtraction is
# positive, negative or zero

'''
INPUT:

Enter first number: 10
Enter second number: 20

OUTPUT:
---------------------------
DIFFERENCE : 10
The result is negative

'''

# input
a = int(input("Enter first number: "))

b = int(input("Enter second number: "))

# process
res = a - b

# output
print('-'*50)

print("DIFFERENCE: ", abs(a-b))

if (res > 0):
    print("THe result is positive")
elif(res < 0):
    print("The result is negative")
else:
    print("The result is zero")
    






