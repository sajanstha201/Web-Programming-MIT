n=int(input("Enter the number of student: "))
class Student:
    def __init__(self,name,roll,department,address,gender,marks):
        self.name=name
        self.roll=roll
        self.department=department
        self.address=address
        self.gender=gender
        self.marks=marks
student_list=[]
for i in range(n):
    ob=Student(
        input("Enter student name:"),
        input("Enter student roll no:"),
        input("Enter Department: "),
        input("Enter address: "),
        input("Enter Gender: "),
        list(map(int,input("Enter marks for three subject: ").split(' ')))
    )
    student_list.append(ob)
max=min=0

for e in student_list:
   for m in e.marks:
        if(max<m):
           max=m
        if(min>m):
            min=m
                 
for e in student_list:
    for m in e.marks:
        if(m==max):
            print("Max Number Student:",e.name)
        if(m==min):
            print("Min Number Student:",e.name)
        if(m<10):
            print("Fail Student: ",e.name)