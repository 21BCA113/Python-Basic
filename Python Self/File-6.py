#arithmetic Operators
print("\n Arithmetic Operators : \n")
A = (5+5)           #Ye Plus karne k liye h
print(A)
A = (5-4)           #Ye Minus Karne K Liye h
print(A)
A = (5*5)           #Ye Multiplication K liye h 
print(A)
A = (5/5)           #Ye Division K liye h
print(A)



#assignment operators 
print("\n Assignment Operators : \n")

a = 5           #Isme a Ki Value Define Ki Hai
print(a)
a += 2          #Isme a Ki Previous Value me 2 ka Increase Hoga 
print(a)
a -= 2          #Isme a Ki Previous Value me 2 Ka Decrease hoga
print(a)
a *= 2          #Isme a Ki Previous Value me 2 Multiply Hoga
print(a)
a /= 2          #Isme a ki Previous Value Me 2 Divide HOga
print(a)

#Comparison Operators ko boolean kehte h Or ye Logic Based hoti h. To Boolean ka answer sirf True YA false me hi aata hai
print("\n Comparison Operators : \n")

b = (14<=7)             #Agar 14 number 7 ya 7 se chhota h to Value True Ayegi. Ans = False
print(b)
b = (14>=7)             #Agar 14 number 7 ya 7 se bada h to value True Ayegi. Ans = True
print(b)                    
b = (14<7)              #Agar 14 number 7 se chhota h like 1 se 6 k ander to True Ayegi. Ans = False
print(b)
b = (14>7)              #Agar 14 number 7 se bada h like 8 se Infinity tak me koi bhi to True Ayegi. Ans = True
print(b)
b = (14==7)             #Agar Number 14 Hi 7 Number h To Value True Ayegi. Ans = False            
print(b)
b = (14!=7)             #Agar Number 14, Number 7 Nahi h to Value True Ayegi. Ans = True
print(b)



# Logical Operators
print("\n Logical Operators : \n")

Boolean_A = True
Boolean_B = False

print("ok",Boolean_A and Boolean_B)  #And K case me Agar Dono True Honge TO Hi Answer True Hoga. Ans = False
print("loda benchod",Boolean_A or Boolean_B)   #Or K Case me Agar dono me se 1 Bhi True Hoga to Answer True Ayega. Ans = True
print(not Boolean_A)            #not k case me Jo Hoga Us Se Ulta answer Dega. True hoga to False
print(not Boolean_B)            #False Hoga True