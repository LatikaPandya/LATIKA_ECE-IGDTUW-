punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
str=input("enter string : ")
no_punct = ""
for char in str:
   if char not in punctuations:
       no_punct = no_punct + char
print("string without punctuation marks : ",no_punct)