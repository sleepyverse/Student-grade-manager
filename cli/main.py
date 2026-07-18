
Students=int(input("Enter the number of students: "))
Student={}
for i in range(Students):
  
    name=input("Enter student name: ")
    Student[name]=[]
    print(Student)
    Subjects=int(input("You want to enter marks of how many subjects?"))
    for j in range(Subjects):
       Marks=int(input('Enter marks of your subjects'))
       Student[name].append(Marks)

    print(Student)

    Average=sum(Student[name])/len(Student[name])
    print("Average of ",name," marks is: ",Average)

highestavg=0
lowestavg=99
for name,Marks in Student.items():
    Avg=sum(Student[name])/len(Student[name])
    if(Avg>highestavg):
       highestavg=Avg
       Topstudent=name
    
    if(Avg<lowestavg):
        lowestavg=Avg
        lowerstudent=name

print("Student with lowest avg score is:",lowerstudent)     
print("Student with highest average score is: ",Topstudent)

file=open("main.txt","w")
for names,marks in Student.items():
    marksline=",".join(str(m) for m in marks )
    file.write(names + ","+marksline+"\n")

file.close()
print("File saved successfully")
