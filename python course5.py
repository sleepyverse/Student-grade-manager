count=0
while count<5:
    print("hello world",count)
    count+=1

i=12
while i>=1:
    print(i)
    i-=1

print("loop ended")



i=0
while i<=10:
   if(i%2==0):
      i+=1
      continue
   print(i)
   i+=1

ch="AQSA IBRAHEEM"
for char in ch:
    if(char=="A"):
        print("A found")
        break
    print(char)
else:
    print("string ends")

for i in range( 1,10,2):
    print(i)

b=int(input("enter your number"))
for i in range(1,11):
    print(b,"*",i,"=",b*i)