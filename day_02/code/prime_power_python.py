# input
n = int(input("Enter a number: "))

# process/output

if(all([ n % i != 0 for i in range(2, n)])):
    print("The number is prime")
else:
    print("The number is not prime")

    