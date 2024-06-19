num1=(input("enter first number : "))
count=0
lst=list(num1)
for i in lst:
    count=count+int(i)
print("sum of digits of a number : ",count)