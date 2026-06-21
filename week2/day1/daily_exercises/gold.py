# # Exercise 1


# 1. Ask the user to input a month (1 to 12).
# 2. Display the season of the month received:
# - Spring runs from March (3) to May (5)
# - Summer runs from June (6) to August (8)
# - Autumn runs from September (9) to November (11)
# - Winter runs from December (12) to February (2)

month = int(input("Enter a month (1-12): "))

if month >= 3 and month <= 5:
    print("Spring")
elif month >= 6 and month <= 8:
    print("Summer")
elif month >= 9 and month <= 11:
    print("Autumn")
else:
    print("Winter")

# # Exercise 2

# Write a for loop to print all numbers from 1 to 20, inclusive.
# Write another for loop that prints every number from 1 to 20 where the index is even. 

for i in range(1, 21):
    print(i)

for i in range(1, 21, 2):
    print(i)

# # Exercise 3
# Write a while loop that keeps asking the user to enter their name.
# Stop the loop if the user’s input is your name. 

name = input("Enter your name: ")

while name != "AKA":
    name = input("Enter your name: ")

print("Hello, AKA!")

# # Exercise 4


# Ask a user for their name, if their name is in the names list print out the index of the first occurrence of the name.
# Example: if input is Cortana we should be printing the index 1

names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']

name = input("Enter your name: ")

if name in names:
    index = names.index(name)
    print(f"{name} is at index {index}")

# # Exercise 5

# Ask the user for 3 numbers and print the greatest number.


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

if num1 > num2 and num1 > num3:
    greatest = num1
elif num2 > num1 and num2 > num3:
    greatest = num2
else:
    greatest = num3
print(f"The greatest number is: {greatest}")

# # Exercise 6

# Demandez à l’utilisateur d’entrer un chiffre de 1 à 9 (y compris).
# Prends un nombre aléatoire entre 1 et 9. Indice : module aléatoire.
# Si l’utilisateur devine le bon numéro, affiche un message indiquant « Gagnant ».
# Si l’utilisateur devine le mauvais numéro, affichez un message disant « Bonne chance la prochaine fois. »
# Bonus : utilisez une boucle qui permet à l’utilisateur de continuer à deviner jusqu’à ce qu’il veuille arrêter.
# Bonus 2 : en quittant la boucle, comptez et affichez le total des parties gagnées et perdues.

import random   
number = random.randint(1, 9)

guess = int(input("Enter a number between 1 and 9: "))

while guess != number:
    print("Wrong guess. Try again.")
    guess = int(input("Enter a number between 1 and 9: "))

print("You won!")


    

