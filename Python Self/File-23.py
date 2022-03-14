# a = ["Ankit","Sneha","Sneha","Dev","Krishna","Apurv","Priya","Zeba","Vaidehi"]
l = [10,20,30,20,30,40,50]
l2 = []
print("Elements : ",len(l))

for i in l:
    if i in l2:
        pass
    else:
        l2.append(i)
print(l)
print(l2)

l2.pop()
print(l2)

del(l[0])
print(l)

k = l.remove()
print(k)
print(l)