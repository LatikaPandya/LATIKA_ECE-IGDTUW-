str=input("enter string : ")
freq={}
for i in str:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
print("Count of all characters in ",str," is : \n",
      freq)