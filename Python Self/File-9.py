# Sum Karne K lIye Ka Code

a = input("A Ki value De re Baba : ")           #User se "a" nam ka Input le rha hu
b = input("B ki value De re Baba : ")           #user se "b" nam ka Input le rha hu
c = a + b                                       #Yaha dekh le string ko integer me convert nhi krega to kya hoga wo
print("Integer me convertt nahi karega to esa hoga addition = ", c)     #yaha output h uske upar wale ka
a = int(a)      #yaha a ki new Value assign hui h jo purani value ko integer me change karega
b = int(b)      #yaha b ki new Value assign hui h jo purani value ko integer me change karega
c = a + b       #Addition
print("Addition = ", c)
c = a - b       #Substraction
print("Substraction = ", c)
c = a * b       #Multiplication
print("Multiplication = ", c)
c = a / b       #Division
print("Division = ", c)
print("Division ki Shesh = ", a%b)  #Bhagakar wali Shesh Yaha milegi ese

#thoda advanced convert karana hai to esa kar skta h dekh le niche

a = int(input("\nyaha pe value Likh Bsdk a Ki : "))       #\n is se new Line Ayegi
b = int(input("\nyaha pe value Likh Bsdk b Ki : "))

print("A + B = ", a + b)            #Value Print karate time Kabhiiiiii bhi Comma Ko Bhulna Mat