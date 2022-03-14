#tuple
#NOTE : You can not change tuple record like the list
t = ()          #it is also a tuple
print(t)

t = (1,)        #use comma if you want only 1 element in tuple
print(t)

t = (1,2,5,6,5,7)       #tuple list
print(t)

t = (1,1,1,1,1,1,2,4,5)
print(t.count(1))       #X.count()  prints how many 1 is in the tuple list

print(t.index(4))       #X.index()  prints where the given number is placed
