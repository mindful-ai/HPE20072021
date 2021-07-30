def getnumbers():
    # return list(range(5))
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

# --------------------------

r = getnumbers()

for i in r:
    print(i)

print("-"*60)



r = getnumbers() # Un-comment this to request/generate data

for i in r:
    print(i)

print("-"*60)


r = getnumbers()

print(next(r))
print(next(r))
print(next(r))

print("Entering for...")

for i in r:
    print(i)



