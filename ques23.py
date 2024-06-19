tempurature=float(input("enter temperture : "))
unit=input("unit of temperature : ")
if unit=="C" or unit=="c":
    temp=(9*tempurature)/5+32
    print("tempurature in fahrenheit is {} degrees".format(temp))
elif unit=="F" or unit=="f":
    temp=5/9*(tempurature-32)
    print("tempurature in celcius is {} degrees".format(temp))
else:
    print("wrong information")