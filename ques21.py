str=input("enter string : ")
lt=list(str)
element=input("enter element whose occurence is to be count : ")
count=0
for i in lt:
    if i==element:
        count+=1
    else:
        continue
print("the number of times the above element occured in the string :",
      count)