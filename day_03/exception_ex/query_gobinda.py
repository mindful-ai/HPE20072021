#1234%$AbcD
import re
password = "1234%$AbcD"
while True:
    p = input("Enter your password: ")
    if(re.search("\d\d\.\d\d", p)):
        print("Access Granted")
        break
    print("Access Denied! Input password which has dd.dd format")

print("You have logged into the system")


