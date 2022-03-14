#string Slicing
'''
            A N K I T       if a string is given python reads as 
            0 1 2 3 4       forward order is started from first. like 0 will be known as A
           -5-4-3-2-1       backword order is started from last to backwards
'''




greeting = "Hello Sir, "
name = "Ankit"
#print(type(name))          #output willbe <class : str>
c = greeting + name
print(c)

print(greeting[:4]) #Here it works like [0:4]
print(greeting[0:5] +" ",name[0:5] +" ",greeting[ 6:9])



#string functions
sup = "hey My name is Ankit How you are doing today"
print(len(sup))         #len() used for string length
print(sup.endswith("today"))  #XXX.endswith()   this function is used to ask boolean if it ends with somthing or not. Ans = True
print(sup.count("i"))         #XXX.count("xyz...")    this function is used for counting the given word in a given line
print(sup.capitalize())       #XXX.capitalize()   this funciton capitalizes first word of the string
print(sup.find("Ankit"))      #XXX.find()      this function only tells if a word exists in a sting and if it exists then it will give its number where it exists of if doesn't exists it will give -1
print(sup.replace("Ankit","Jarvis"))    #XXX.replace()   i know you got it what it does and if you didn't got it then i will let you know that it replaces the first given name with the another given name from the whole string
