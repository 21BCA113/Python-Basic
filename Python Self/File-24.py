s = "Om Sai Ram"
print(len(s))
a = 0
for  i in s:
    if i == 'a' or i == 'A' or i == 'e' or i == 'E' or i == 'i' or i == 'I ' or i == 'o' or i == 'O' or i == 'u' or i=='U':
        a = a + 1
print("There are {} Vovels".format(a))