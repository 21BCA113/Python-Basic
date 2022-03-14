#list 

a = [1,6,3,5,66,43,4634,45]
print(a)

# access using index

a[2] = 23      #used to change value in linst using index
print(a[3])

b = [56, "Ak", 6.9, False] #this is how you can also create a list with all type
print(b)

persons = ["Ak","Michel","Lucifer","ayush","rajveer","vishal","meet"]
print(persons[0:3])
print(persons[:4])
print(persons[-2])

#Sort list

list = [1,5,566,767,6,676,575,676,756,756,5,43,645,3,4,7,67,6,876,854,35]
print(list)
list.sort()         #sort in accending order
print(list)
list.reverse()      #sort in decending order
print(list)
list.append(56)     #adds something in list 56 will be added
print(list)
list.pop(3)         #list se 3rd index wale ko remove karne k liye 
print(list)
list.remove(6)      #list se 6 ko remove karne k liye
print(list)
list.insert(3,5)   # list k ander ye sare add honge
print(list)
print(list.count(1))