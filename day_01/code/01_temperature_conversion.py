# Input temperature in celcius from the user and convert it to farenheit

'''
INPUT:
celcius <- 100

OUTPUT:
------------------------------------------------
100 degree celcius is 212 degrees in farenheit

INFO:
°F = (°C × 9/5) + 32
'''

# input
c = input("celcius <- ")

# process
c = float(c)
f = c * (9/5) + 32

# output
print("------------------------------------------------")
print("%.2f degree celcius is %.2f degree farenheit" % (c, f))
