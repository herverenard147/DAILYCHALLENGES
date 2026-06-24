Exercice 1 : Création d'un tableau 1D
import numpy as np

# On crée un tableau avec les nombres de 0 à 9
array1 = np.arange(0, 10)

print(array1)

Exercice 2 : Conversion de type
import numpy as np

# On part d'une liste Python normale
liste = [3.14, 2.17, 0, 1, 2]

# On la convertit en tableau NumPy
array2 = np.array(liste)

# On convertit les nombres décimaux en nombres entiers
array2 = array2.astype(int)

print(array2)

Exercice 3 : Tableau 3x3
import numpy as np

# On crée d'abord les nombres de 1 à 9
array3 = np.arange(1, 10)

# Puis on transforme ce tableau en une grille de 3 lignes et 3 colonnes
array3 = array3.reshape(3, 3)

print(array3)

Exercice 4 : Tableau 2D avec des nombres aléatoires
import numpy as np

# On crée un tableau de forme (4 lignes, 5 colonnes)
# rempli de nombres aléatoires entre 0 et 1
array4 = np.random.rand(4, 5)

print(array4)

Exercice 5 : Sélectionner une ligne

import numpy as np

array5 = np.array([[21,22,23,22,22],
                    [20, 21, 22, 23, 24],
                    [21,22,23,22,22]])

# En Python, on compte à partir de 0
# Donc la "deuxième ligne" a l'index 1
deuxieme_ligne = array5[1]

print(deuxieme_ligne)

Exercice 6 : Inverser un tableau

import numpy as np

array6 = np.arange(0, 10)

# [::-1] veut dire : on parcourt le tableau à l'envers
array6_inverse = array6[::-1]

print(array6_inverse)

Exercice 7 : Matrice identité

import numpy as np

# np.eye() crée une matrice identité (des 1 sur la diagonale, des 0 ailleurs)
array7 = np.eye(4)

print(array7)

import numpy as np

array8 = np.arange(1, 10)  # tableau de 1 à 9

somme = np.sum(array8)
moyenne = np.mean(array8)

print(f"Sum: {somme}, Average: {moyenne}")

Exercice 8 : Somme et moyenne

import numpy as np

array8 = np.arange(1, 10)  # tableau de 1 à 9

somme = np.sum(array8)
moyenne = np.mean(array8)

print(f"Sum: {somme}, Average: {moyenne}")

Exercice 9 : Créer puis reshaper un tableau

import numpy as np

# On crée les nombres de 1 à 20
array9 = np.arange(1, 21)

# On transforme en grille de 4 lignes et 5 colonnes
array9 = array9.reshape(4, 5)

print(array9)

Exercice 10 : Sélection conditionnelle (nombres impairs)

import numpy as np

array10 = np.arange(0, 10)

# La condition array10 % 2 != 0 vérifie si le reste de la division par 2 n'est pas 0
# Si le reste n'est pas 0, c'est un nombre impair
nombres_impairs = array10[array10 % 2 != 0]

print(nombres_impairs)
