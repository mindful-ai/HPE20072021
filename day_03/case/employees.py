D = {}
while True:
    
    # input
    name = input("Employee Name: ")
    
    if(name == 'quit'):
        break
    age = input("Employee Age: ")
    salary = input("Employee salary: ")

    # process

    hike = float(salary) * 0.17
    newsalary = float(salary) + hike

    # output

    print("-" * 50)
    print("New Salary after 17% hike", newsalary)
    D['name'] = {'name':name, 'age': age, 'salary':newsalary}

print(D)


# Rajesh 35 1300000
# Anil   35 1200500
# Sunil  36 1450000
# ...