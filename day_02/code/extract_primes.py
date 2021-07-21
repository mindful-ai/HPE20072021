# project B

# Write a program to input several numbers from the user
# and extract the prime numbers from the list

'''
Input: 12 23 34 45 56 67 12 31 13
Output: 23 67 31 13
'''

import primemodule

print("extract_primes.py ", __name__)
# input

ns = input("Enter the number separated by space: ")

# process

ns = ns.split()
primes = []
for n in ns:
    if(primemodule.checkprime(int(n)) == True):
        primes.append(n)


# output
print("PRIMES: ", ' '.join(primes))