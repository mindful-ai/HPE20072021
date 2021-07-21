def checkprime(n):
    for i in range(2, n):
        if(n % i == 0):
            return False
    return True

# ---------------------------------

print("primemodule.py ", __name__)

if __name__ == "__main__":
    
    # input
    n = int(input("Enter a number: "))

    # output
    if(checkprime(n) == True):
        print("The number is prime")
    else:
        print("The number is not prime")