#Défi 1
#Ask the user for a number and a length.
#Create a program that prints a list of multiples of the number until the list length reaches length.


number=int(input("Entrez un nombre :   "  ))
length=int(input("Entrez une longueur :   "  ))
multiples=[]
for i in range(1,length+1):
    multiples.append(number*i)
print(multiples)



#Défi 2
#Write a program that asks a string to the user, and display a new string with any duplicate consecutive letters removed.


word = input("Entrez un mot : ")

result = ""
for i in range(len(word)):
    if i == 0 or word[i] != word[i-1]:
        result += word[i]

print(result)