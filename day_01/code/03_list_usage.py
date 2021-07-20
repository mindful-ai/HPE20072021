# Program to calculate the average of 5 numbers


'''
Input
# 10
# 20
# 30
# 40
# 50

Output
Average = 30
'''

# input

N = []
L = [1, 2, 3, 4, 5]
for i in L:
    uin = int(input("# "))
    N.append(uin)

# process
print(N)
avg = sum(N)/len(N)

# output
print("Average = ", avg)
