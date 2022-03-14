
#program to enter name in letter

letter="Hey <|NAME|> how are You. Is that your correct Birthdate <|BDATE|>"
name = input("Enter Your Name\n")
date = input("Enter Your Birthdate\n")
letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|BDATE|>", date)
print(letter + "\n\n\n\n")