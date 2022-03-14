#Sorted marks of students

m1 = int(input("Enter Marks of Student 1 : "))
m2 = int(input("Enter Marks of Student 2 : "))
m3 = int(input("Enter Marks of Student 3 : "))
m4 = int(input("Enter Marks of Student 4 : "))
m5 = int(input("Enter Marks of Student 5 : "))
m6 = int(input("Enter Marks of Student 6 : "))
m7 = int(input("Enter Marks of Student 7 : "))
m8 = int(input("Enter Marks of Student 8 : "))

list = [m1,m2,m3,m4,m5,m6,m7,m8]        #this is a list don't take tuple here it is not modifyable
list.sort()
print(list)