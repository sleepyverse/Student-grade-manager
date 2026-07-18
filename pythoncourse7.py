a=open("demo.txt","r")
data=a.read(4)
print(data)
a.close()


f=open("wor.txt","r")
line=f.readline()
print(line)
f.close()

s=open("wor.txt","w")
d=s.write("mera nam aqsa hai")

print(d)

v=open("wor.txt","a")
n=v.write("aqsaaaaaaaaaaaaaaaaaaaa")
print(v)

b=open("org,txt","w+")
#c=b.write("open it")
print(b.read())


with open("aqsa.txt","r")as c:
   m=c.read()
   print(m)

import os
os.remove("demo.txt")