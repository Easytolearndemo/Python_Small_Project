import string
import random

s1=string.ascii_lowercase #a...z
#print(s1)
s2=string.ascii_uppercase #A....Z
#print(s2)
s3=string.digits   #0...9
#print(s3)
s4=string.punctuation #!@#$....
#print(s4)

plen=int(input("Enter your password length:"))

s=[]

s.extend(list(s1))
s.extend(list(s2))
s.extend(list(s3))
s.extend(list(s4))
#print(s)


random.shuffle(s)
#print(s)
print("your password is:")

print("".join(s[0:plen]))

