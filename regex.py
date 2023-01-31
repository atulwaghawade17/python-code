import re

#txt='the rain in spain'
#x=re.search("^the.*spain$",txt)
#print(x)

n=input(" ")
pattern="[1-4]{1}[a-zA-Z]{2}[0-9]{2}[a-zA-Z]{2}[0-9]{3}"
pattern1="[1-4]{1}[a-zA-Z]{2}[0-9]{2}[a-zA-Z]{3}[0-9]{2}"

x=re.match(pattern, n)
y=re.match(pattern1,n)
if x:
    print("UG USN")
elif y:
    print("PG USN")
else:
    print("invalid number")
