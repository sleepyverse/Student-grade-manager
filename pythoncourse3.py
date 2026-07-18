Marks=[12.3,45.8,46.9,23.67,8.9]
print(Marks)
print(type(Marks))

print(Marks[4])
print(Marks[0 : 3])

print(len(Marks))


Student=["aqsa",21,5.2,"female"]
print(Student)

Student[0]="ayesha"
print(Student)

print(Student[-3:-1])


num=[1,2,3]
num.append(4)
print(num)

list.sort(num)
print(num)
list.sort(num,reverse=True)
print(num)

list.sort(Marks)
print(Marks)
list.reverse(Marks)
print(Marks)

list.insert(Marks,2,100)
print(Marks)

list.remove(Marks,100)
print(Marks)

list.pop(Marks,1)
print(Marks)


tup=(1,2,3,4,5,5,6,7,8,9,10,11)
print(type(tup))

tuple=()
print(tuple)