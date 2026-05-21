# Défi 1 : Dictionnaire index des lettres
# But : Créez un dictionnaire qui stocke les indices (nombre de la position) de chaque lettre dans un mot fourni par l’utilisateur (entrée()).



# Sujets clés de Python :

# Entrée utilisateur (input())
# Dictionnaires
# Boucles (boucle)for
# Énoncés conditionnels (, ifelse)
# Manipulation des cordes
# Listes


# Instructions :
# 1. Entrée utilisateur :

# Demandez à l’utilisateur d’entrer un mot.
# Stockez le mot d’entrée dans une variable.
# 2. Création du dictionnaire :

# Itérez chaque caractère du mot d’entrée en utilisant une boucle.
# Et vérifiez si le caractère est déjà une clé dans le dictionnaire.

#     * If it is, append the current index to the list associated with that key.
#     * If it is not, create a new key-value pair in the dictionary.
# Assurez-vous que les caractères (touches) sont des chaînes de caractères.
# Assurez-vous que les indices (valeurs) sont stockés dans des listes.
# 3. Production attendue :

# Pour l’entrée « dodo », la sortie doit être : .{"d": [0, 2], "o": [1, 3]}
# Pour l’entrée « froggy », la sortie devrait être : .{"f": [0], "r": [1], "o": [2], "g": [3, 4], "y": [5]}
# Pour les « raisins » d’entrée, la sortie devrait être : .{"g": [0], "r": [1], "a": [2], "p": [3], "e": [4], "s": [5]}


user_input = input("Enter a word: ")
result = {}

for i, char in enumerate(user_input):
    if char in result:
        result[char].append(i)
    else:
        result[char] = [i]

print(result)




# Défi 2 : Articles abordables
# But : Créez un programme qui imprime une liste d’articles pouvant être achetés avec un montant donné.



# Sujets clés de Python :

# Dictionnaires
# Boucles (boucle)for
# Énoncés conditionnels (, ifelse)
# Manipulation de chaînes (replace())
# Conversion de type (int())
# Listes
# Tri (sorted())


# Instructions :
# 1. Stocker les données :

# Vous recevrez un dictionnaire () où les clés sont les noms des articles et les valeurs sont leurs prix (sous forme de chaînes avec un signe dollar). La priorité est définie par la position de l’iten dans le dictionnaire : du plus important au moins important.items_purchase
# On vous verra également une chaîne () représentant le montant d’argent dont vous disposez.wallet
# 2. Nettoyage des données :

# Il faut nettoyer le signe dollar et les virgules avec Python. Ne le code pas dur.
# 3. Détermination des articles abordables :

# Créez une liste appelée et ajoutez les articles que vous pouvez acheter avec l’argent que vous avez dans votre portefeuillebasket
# N’oubliez pas de mettre à jour le portefeuille après avoir acheté un article.
# Si le est vide (aucun objet n’est disponible), retournez la chaîne « Nothing ».basket
# Sinon, imprimez la liste par ordre alphabétique.basket
# 4. Exemples :

# Données :
# items_purchase = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}
# wallet = "$300"


# La sortie devrait être : .["Bread", "Fertilizer", "Water"]

# Données :
# items_purchase = {"Apple": "$4", "Honey": "$3", "Fan": "$14", "Bananas": "$4", "Pan": "$100", "Spoon": "$2"}
# wallet = "$100"


# La sortie devrait être : .["Apple", "Bananas", "Fan", "Honey", "Spoon"]

# Données :
# items_purchase = {"Phone": "$999", "Speakers": "$300", "Laptop": "$5,000", "PC": "$1200"}
# wallet = "$1"


# La sortie devrait être : ."Nothing"
items_purchase = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}
wallet = "$300"

basket = []

# Nettoyage du wallet une seule fois
wallet_amount = int(wallet.replace("$", "").replace(",", ""))

for item, price in items_purchase.items():
    # Nettoyage du prix
    price_amount = int(price.replace("$", "").replace(",", ""))
    
    if price_amount <= wallet_amount:
        basket.append(item)
        wallet_amount -= price_amount  # Mise à jour du portefeuille

if len(basket) == 0:
    print("Nothing")
else:
    print(sorted(basket))