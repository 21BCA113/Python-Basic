s = "Om Sai Ram"
v = ('a','A','e','E','i','I','o','O','u','U')
print(len(s))
a = 0
for  i in s:
    if i in v:
        a = a + 1
print("There are {} Vovels".format(a))