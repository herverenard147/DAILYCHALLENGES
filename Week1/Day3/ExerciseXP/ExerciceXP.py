# #Instructions
# # Challenge 1
# #Imprimez le résultat suivant en utilisant une seule ligne de code :
# #Hello world
# #Hello world
# #Hello world
# ##Hello world



from ast import If


print("Hello world:\n"*3)




# # Challenge 2
# #Exercice 2
#Write code that calculates the result of:
#(99^3)*8 (meaning 99 to the power of 3, times 8).
resultat=(99**3)*8
print(resultat)



# Exercice 3
#Instructions
#Predict the output of the following code snippets:
#Coment what is your guess, then run the code and compare


print(5 < 3) #False car 5 est plus grand que 3
print(3 == 3) #True car les deux sont égaux
print(3 == "3") # TypeError impossible de comparer str et int avec 
print("3" > 3) #False car les types sont différents (str et int)
print("Hello" == "hello") #False car les chaînes de caractères sont sensibles à la casse            


#Exercice 4
#Instructions
#Create a variable called computer_brand which value is the brand name of your computer.
#Using the computer_brand variable, print a sentence that states the following:
#"I have a <computer_brand> computer."

computer_brand="Hp"
print(f"I have a {computer_brand} computer.")

#Exercice 5
#Instructions
#Instructions
#Create a variable called name, and set it’s value to your name.
#Create a variable called age, and set it’s value to your age.
#Create a variable called shoe_size, and set it’s value to your shoe size.
#Create a variable called info and set it’s value to an interesting sentence about yourself. The sentence must contain all the variables created in parts 1, 2, and 3.
#Have your code print the info message.
#Run your code.


name="Lylda"
age=21
shoe_size=38
info=f"My name is {name}, I am {age} years old and my shoe size is {shoe_size}."
print(info)

##Exercise 6
#Instructions
#Create two variables, a and b.
#Each variable’s value should be a number.
#If a is bigger than b, have your code print "Hello World".
a=15
b=7
if a>b :
    print("Hello world")


#Exercice 7
#Instructions
#Write code that asks the user for a number and determines whether this number is odd or even.

nombre=input("Entrez un nombre :   "  )
if (int(nombre)%2 ==0):
    print("Le nombre est pair")
else:    print("Le nombre est impair")


#Exercice 8
#Instructions
#Write code that asks the user for their name and determines whether or not you have the same name. Print out a funny message based on the outcome.
nom1=input("Entrez votre nom :   "  )
nom2="Lylda"            
if nom1==nom2:
    print("You , c'est le même nom!")   

else:    print("Oups, les noms sont différents, reessayez !")    

#Exercise 9
#Write code that will ask the user for their height in centimeters.
#If they are over 145 cm, print a message that states they are tall enough to ride.
#If they are not tall enough, print a message that says they need to grow some more to ride.

taille=int(input("Entrez votre taille en cm :   "  ))
if taille>145:
    print("Vous êtes assez grand pour faire du manège !")   
else:    print("Vous devez grandir un peu plus pour faire du manège !")