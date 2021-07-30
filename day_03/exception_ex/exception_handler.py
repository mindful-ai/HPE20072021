try:
    n = input("Enter a number: ")
    d = {}
    p = int(n) ** 2
    #print(d['number'])
    #x = 1/0
except ValueError:
    print("Invalid value for conversion")
except KeyError:
    print("Invalid key entered")
except Exception as E:
    print("Exception message - ", E)
else:
    print("Result :", p)
finally:
    print("Thank you!")