Exercice 1 : Opérations sur les matrices

import numpy as np

# On crée une matrice 3x3
A = np.array([[2, 1, 1],
              [1, 3, 2],
              [1, 0, 0]])

# 1. Calcul du déterminant
determinant = np.linalg.det(A)
print("Déterminant :", determinant)

# 2. Calcul de l'inverse de la matrice
inverse = np.linalg.inv(A)
print("Inverse :\n", inverse)

Exercice 2 : Analyse statistique

import numpy as np

# On génère 50 nombres aléatoires entiers entre 1 et 100
donnees = np.random.randint(1, 100, size=50)

# 1. Moyenne et médiane
moyenne = np.mean(donnees)
mediane = np.median(donnees)

# 2. Écart-type
ecart_type = np.std(donnees)

print(f"Mean: {moyenne}, Median: {mediane}")
print(f"Standard Deviation: {ecart_type}")

Exercice 3 : Manipulation de dates

import numpy as np

# On crée un tableau de dates pour tout janvier 2023
# du 1er janvier (inclus) au 1er février (exclu)
dates = np.arange('2023-01-01', '2023-02-01', dtype='datetime64[D]')

print(dates)

# Conversion au format YYYY/MM/DD
dates_converties = [str(date).replace('-', '/') for date in dates]

print(dates_converties[:5])  # on affiche les 5 premières

Exercice 4 : Manipulation de données avec NumPy et Pandas

import numpy as np
import pandas as pd

# Création d'un DataFrame 5x4 rempli de nombres aléatoires entre 0 et 100
donnees = np.random.randint(0, 100, size=(5, 4))
df = pd.DataFrame(donnees, columns=['A', 'B', 'C', 'D'])

print(df)
# 1. Sélection conditionnelle : on garde seulement les lignes où la colonne A > 50
selection = df[df['A'] > 50]
print("Lignes où A > 50 :\n", selection)
# 2. Fonctions d'agrégation
print("Somme de chaque colonne :\n", df.sum())
print("\nMoyenne de chaque colonne :\n", df.mean())

Exercice 5 : Représentation d'images

import numpy as np
import matplotlib.pyplot as plt

# Création d'une image 5x5 en niveaux de gris, avec des valeurs aléatoires entre 0 et 255
image = np.random.randint(0, 256, size=(5, 5))

print(image)

# Affichage de l'image
plt.imshow(image, cmap='gray')
plt.title("Image en niveaux de gris 5x5")
plt.colorbar(label="Intensité du pixel (0=noir, 255=blanc)")
plt.show()

Exercice 6 : Test d'hypothèse basique

import numpy as np

np.random.seed(42)  # pour reproduire les mêmes résultats

# Scores de productivité avant la formation
productivity_before = np.random.normal(loc=50, scale=10, size=30)

# Scores de productivité après la formation
productivity_after = productivity_before + np.random.normal(loc=5, scale=3, size=30)
# On calcule la différence entre après et avant, pour chaque employé
difference = productivity_after - productivity_before

# Moyenne et écart-type de ces différences
moyenne_diff = np.mean(difference)
ecart_type_diff = np.std(difference, ddof=1)  # ddof=1 = écart-type "d'échantillon"

n = len(difference)
erreur_standard = ecart_type_diff / np.sqrt(n)

# Statistique de test (t de Student, fait "à la main")
t_stat = moyenne_diff / erreur_standard

print(f"Différence moyenne : {moyenne_diff:.2f}")
print(f"Statistique t : {t_stat:.2f}")

Exercice 7 : Comparaison de tableaux complexes

import numpy as np

array1 = np.array([5, 12, 8, 20, 3])
array2 = np.array([7, 9, 8, 15, 10])

# Comparaison élément par élément : array1 > array2 ?
comparaison = array1 > array2

print(comparaison)

Exercice 8 : Manipulation de séries temporelles

import numpy as np
import pandas as pd

# Génération d'une série temporelle pour toute l'année 2023 (une date par jour)
dates_2023 = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')

# On crée une "fausse" donnée (valeur aléatoire) pour chaque jour
valeurs = np.random.rand(len(dates_2023))

serie = pd.Series(valeurs, index=dates_2023)

print(serie.head())
# Découpage (slicing) par trimestre
janvier_mars = serie['2023-01-01':'2023-03-31']
avril_juin   = serie['2023-04-01':'2023-06-30']
juillet_sept = serie['2023-07-01':'2023-09-30']
octobre_dec  = serie['2023-10-01':'2023-12-31']

print("Janvier à Mars :", len(janvier_mars), "jours")
print("Avril à Juin :", len(avril_juin), "jours")
print("Juillet à Septembre :", len(juillet_sept), "jours")
print("Octobre à Décembre :", len(octobre_dec), "jours")

Exercice 9 : Conversion de données

import numpy as np
import pandas as pd

# 1. NumPy array -> Pandas DataFrame
array_numpy = np.array([[1, 2, 3], [4, 5, 6]])
df = pd.DataFrame(array_numpy, columns=['A', 'B', 'C'])

print("DataFrame :\n", df)
# 2. Pandas DataFrame -> NumPy array
array_retour = df.to_numpy()

print("\nArray NumPy :\n", array_retour)
print("Type :", type(array_retour))

Exercice 10 : Visualisation basique

import numpy as np
import matplotlib.pyplot as plt

# Génération de 50 nombres aléatoires
donnees = np.random.rand(50)

plt.figure(figsize=(10, 5))
plt.plot(donnees, marker='o', linestyle='-', color='teal')

plt.title("Graphique en ligne de nombres aléatoires")
plt.xlabel("Index")
plt.ylabel("Valeur")
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()
