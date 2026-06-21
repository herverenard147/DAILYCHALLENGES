#Ask the user for a number and a length.
#Create a program that prints a list of multiples of the number until the list length reaches length.


age = int(input("Entrez votre age: "))
age = age % 10

bougies = f"__{'i' * age}__"
    
cake = f"""
    {bougies}
|:H:a:p:p:y:|
_|___________|_
|AAAAAAAAAAAAAAAA|
|:B:i:r:t:h:d:a:y:|
|__________________|
~~~~~~~~~~~~~~~~~~~~
"""
print(cake)