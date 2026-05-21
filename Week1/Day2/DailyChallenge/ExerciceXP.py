
# EXERCICE 1 : Utilisation de la fonction zip

# Sujets clés de Python :

# Création de dictionnaires
# Fonction zip ou compréhension du dictionnaire

# Instructions
# On vous donne deux listes. Convertissez-les en dictionnaire où la première liste contient les clés et la seconde liste contient les valeurs correspondantes.


keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

result = dict(zip(keys, values))
print(result)

# EXERCICE 2 : 


# Instructions

# Écris un programme qui calcule le coût total des billets de cinéma pour une famille en fonction de leur âge.

# L’âge des membres de la famille est enregistré dans un dictionnaire.
# Les règles de tarification des billets sont les suivantes :
# Moins de 3 ans : Gratuit
# 3 à 12 ans : 10 $
# Plus de 12 ans : 15 $


# Données familiales :

# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}


# Parcourez le dictionnaire en boucle pour calculer le coût total.family
# Imprimez le prix du billet pour chaque membre de la famille.
# Imprimez le coût total à la fin.


family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
total_cost = 0
for name, age in family.items():
    if age < 3:
        cost = 0
    elif 3 <= age <= 12:
        cost = 10
    else:
        cost = 15
    print(f"{name} : {cost} $")
    total_cost += cost
print(f"Total cost : {total_cost} $")




# Bonus :
# Permettre à l’utilisateur de saisir les noms et âges des membres de la famille, puis de calculer le coût total du ticket.

family = {}

while True:
    name = input("Enter the name of the family member (or 'done' to finish): ")
    if name.lower() == 'done':
        break
    while True:
        try:
            age = int(input(f"Enter the age of {name}: "))
            break
        except ValueError:
            print("Please enter a valid age.")
    family[name] = age

total_cost = 0
for name, age in family.items():
    if age < 3:
        cost = 0
    elif 3 <= age <= 12:
        cost = 10
    else:
        cost = 15
    print(f"{name} : {cost} $")
    total_cost += cost
print(f"Total cost : {total_cost} $")




# EXERCICE 3 : 

# Informations sur la marque :

# name: Zara
# creation_date: 1975
# creator_name: Amancio Ortega Gaona
# type_of_clothes: men, women, children, home
# international_competitors: Gap, H&M, Benetton
# number_stores: 7000
# major_color: 
#     France: blue, 
#     Spain: red, 
#     US: pink, green


# Créez un dictionnaire appelé avec les données fournies.brand
# Modifiez et accédez au dictionnaire comme suit :
# Changez la valeur de à 2.number_stores
# Imprimez une phrase décrivant les clients de Zara à l’aide de la clé.type_of_clothes
# Ajoutez une nouvelle clé avec la valeur .country_creationSpain
# Vérifiez s’il existe et, si oui, ajoutez « Desigual » à la liste.international_competitors
# Supprime la clé.creation_date
# Imprimez le dernier élément dans .international_competitors
# Imprimez les couleurs principales aux États-Unis.
# Imprimez le nombre de clés dans le dictionnaire.
# Imprimez toutes les clés du dictionnaire.

# [Exercice 3] Dans l’Exercice 3, la logique d’ajouter « Desigual » à la liste des concurrents est légèrement incorrecte. L’instruction était de vérifier si la clé existait. Votre code vérifie si la valeur est déjà dans la liste (), ce qui sera faux, donc « Desigual » n’est jamais ajouté. La vérification correcte serait .international_competitors'Desigual'if "Desigual" in brand["international_competitors"]if "international_competitors" in brand:


brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue",
        "Spain": "red",
        "US": ["pink", "green"]
    }
    }



brand["number_stores"] = 2
print(f"Zara sells {', '.join(brand['type_of_clothes'])} clothes.")
brand["country_creation"] = "Spain"
if "international_competitors" in brand:
    if "Desigual" not in brand["international_competitors"]:
        brand["international_competitors"].append("Desigual")
del brand["creation_date"] 
print(brand["international_competitors"][-1])
print(brand["major_color"]["US"])
print(len(brand))
print(list(brand.keys()))


# Bonus :
# Créez un autre dictionnaire appelé avec et . Fusionnez ce dictionnaire avec le dictionnaire original et imprimez le résultat.more_on_zaracreation_datenumber_storesbrand


more_on_zara = {
    "creation_date": 1975,
    "number_stores": 10300
    }
brand.update(more_on_zara)
print(brand)



# Exercice 4 : Un peu de géographie
# But : Créez une fonction qui décrit une ville et son pays.

# Sujets clés de Python :

# Fonctions à paramètres multiples
# Valeurs de paramètres par défaut
# Formatage des chaînes


# Étape 1 : Définir une fonction avec des paramètres

# Définissons une fonction nommée .describe_city()
# Cette fonction devrait accepter deux paramètres : et .citycountry
# Attribuez au paramètre une valeur par défaut, comme « Inconnu ».country


# Étape 2 : Imprimer un message

# À l’intérieur de la fonction, configurez le code pour afficher une phrase comme « is in ».
# Remplacez et par les valeurs des paramètres.<city><country>


# Étape 3 : Appeler la fonction

# Appelez l’événement avec différentes combinaisons de ville et de pays.describe_city()
# Essayez de l’appeler avec et sans fournir l’argument du pays pour voir la valeur par défaut en action.
# Exemple : et .describe_city("Reykjavik", "Iceland")describe_city("Paris")


# Résultats attendus :

# Reykjavik is in Iceland.
# Paris is in Unknown.


def describe_city(city, country="Unknown"):
    print(f"{city} is in {country}.")    
describe_city("Reykjavik", "Iceland")
describe_city("Paris")



# Exercice 5 : Aléatoire

# But : Créez une fonction qui génère des nombres aléatoires et les compare.

# Sujets clés de Python :

# random Module
# random.randint() Fonction
# Énoncés conditionnels (, ifelse)


# Étape 1 : Importer le module aléatoire

# Au début de votre script, utilisez pour accéder aux fonctions de génération de nombres aléatoires.import random


# Étape 2 : Définir une fonction avec un paramètre

# Créez une fonction qui accepte un nombre compris entre 1 et 100 comme paramètre.


# Étape 3 : Générer un nombre aléatoire

# À l’intérieur de la fonction, on utilise pour générer un entier aléatoire entre 1 et 100.random.randint(1, 100)


# Étape 4 : Comparez les chiffres

# Si c’est pareil, imprimez un message de réussite. Sinon, affichez un message d’échec et affichez les deux chiffres.


# Étape 5 : Appeler la fonction

# Appelez la fonction avec un nombre compris entre 1 et 100.


# Résultats attendus :

# Success! (if the numbers match)
# Fail! Your number: 50, Random number: 23 (if they don't match)

import random

def compare_numbers(number):
    random_number = random.randint(1, 100)
    if number == random_number:
        print("Success!")
    else:
        print(f"Fail! Your number: {number}, Random number: {random_number}")
compare_numbers(50) 




# Exercice 6 : Créons des t-shirts personnalisés !

# But : Créez une fonction pour décrire la taille et le message d’un t-shirt, avec les valeurs par défaut.

# Sujets clés de Python :

# Fonctions avec paramètres et valeurs par défaut
# Arguments de mots-clés


# Étape 1 : Définir une fonction avec des paramètres

# Définissons une fonction appelée .make_shirt()
# Cette fonction devrait accepter deux paramètres : et .sizetext


# Étape 2 : Imprimer un message résumé

# Configurez la fonction pour afficher une phrase résumant la taille et le message du maillot.


# Étape 3 : Appeler la fonction



# Étape 4 : Modifier la fonction avec les valeurs par défaut

# Modifie la fonction pour qu’elle ait pour valeur par défaut « grand » et pour valeur par défaut « J’adore Python ».make_shirt()sizetext


# Étape 5 : Appeler la fonction avec valeurs par défaut et personnalisées

# On appelle pour faire un grand t-shirt avec le message par défaut.make_shirt()
# On demande de créer un t-shirt moyen avec le message par défaut.make_shirt()
# Appelez pour fabriquer une chemise de n’importe quelle taille avec un message différent.make_shirt()


# Étape 6 (bonus) : Arguments de mots-clés
# Appelez en utilisant des arguments de mots-clés (par exemple, ).make_shirt()make_shirt(size="small", text="Hello!")

# Résultats attendus :

# The size of the shirt is large and the text is I love Python.
# The size of the shirt is medium and the text is I love Python.
# The size of the shirt is small and the text is Custom message.


def make_shirt(size="large", text="I love Python"):
    print(f"The size of the shirt is {size} and the text is {text}.")    
make_shirt()
make_shirt("medium")
make_shirt("small", "Custom message")
make_shirt(size="small", text="Hello!")



# Exercice 7 : Conseils sur la température

# But : Générez une température aléatoire et donnez des conseils en fonction de la plage de température.

# Sujets clés de Python :

# Fonctions
# Conditionnels (if / elif)
# Nombres aléatoires
# Nombres en virgule flottante (bonus)
# Saisons de manipulation (bonus)


# Étape 1 : Créer la fonction get_random_temp()

# Créez une fonction appelée qui renvoie un entier aléatoire entre -10 et 40 degrés Celsius.get_random_temp()


# Étape 2 : Créer la fonction principale()

# Créer une fonction appelée . À l’intérieur de cette fonction :main()
# Appelle pour obtenir une température aléatoire.get_random_temp()
# Stockez la température dans une variable et imprimez un message amical du type :
# « La température actuelle est de 32 degrés Celsius. »


# Étape 3 : Fournir des conseils basés sur la température

# À l’intérieur, donnez des conseils basés sur la température :main()
# En dessous de 0°C : par exemple, « Brrr, c’est glacial ! Mets des couches supplémentaires aujourd’hui. »
# Entre 0°C et 16°C : par exemple, « Il fait assez frais ! N’oublie pas ton manteau. »
# Entre 16°C et 23°C : par exemple, « Beau temps ».
# Entre 24°C et 32°C : par exemple, « Un peu chaud, restez hydraté. »
# Entre 32°C et 40°C : par exemple, « Il fait vraiment chaud ! Reste calme. »


# Étape 4 : Températures en virgule flottante (bonus)

# Modifier pour retourner un nombre en virgule flottante aléatoire en utilisant des valeurs de température plus précises.get_random_temp()random.uniform()


# Étape 5 : Saisons par mois (bonus)

# Au lieu de générer directement une température aléatoire, demandez à l’utilisateur un mois (1-12) et déterminez la saison en utilisant / conditions.ifelif
# Modifiez pour indiquer des températures spécifiques à chaque saison.get_random_temp()


# Résultats attendus :

# The temperature right now is 32 degrees Celsius.
# It's really hot! Stay cool.

import random

def get_random_temp():
    return random.uniform(-10, 40)  

def main():
    temp = get_random_temp()
    print(f"The temperature right now is {temp:.1f} degrees Celsius.")
    if temp < 0:
        print("Brrr, it's freezing! Wear extra layers today.")
    elif 0 <= temp < 16:
        print("It's quite chilly! Don't forget your coat.")
    elif 16 <= temp < 24:
        print("Nice weather.")
    elif 24 <= temp < 32:
        print("A bit warm, stay hydrated.")
    else:
        print("It's really hot! Stay cool.")

main()


# Exercice 8 : Garnitures de pizza

# Sujets clés de Python :

# Boucles
# Listes
# Formatage des chaînes


# Instructions :

# Écrivez une boucle demandant à l’utilisateur d’entrer les garnitures une par une.
# Arrêtez la boucle lorsque l’utilisateur tape . 'quit'
# Pour chaque garniture saisie, imprimez :
# "Adding [topping] to your pizza."
# Après avoir quitté la boucle, imprimez toutes les garnitures et le coût total de la pizza.
# Le prix de base est de 10 $, et chaque topping ajoute 2,50 $.

toppings = []
while True:
    topping = input("Enter a pizza topping (or 'quit' to finish): ")
    if topping.lower() == 'quit':
        break
    toppings.append(topping)
    print(f"Adding {topping} to your pizza.")

total_cost = 10 + len(toppings) * 2.5
print(f"Your pizza has the following toppings: {', '.join(toppings)}.")
print(f"The total cost is ${total_cost:.2f}.")