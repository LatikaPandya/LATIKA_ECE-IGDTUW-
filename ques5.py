str=input('enter text : ')
f=open("ques5file.txt", "a")
for line in str: 
    f.write(line)
print("done!")