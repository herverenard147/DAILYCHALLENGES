# ==========================================
# Création de la classe Farm
# ==========================================

class Farm:

    # ==========================================
    # Constructeur
    # ==========================================
    def __init__(self, farm_name):

        # Nom de la ferme
        self.name = farm_name

        # Dictionnaire vide pour stocker les animaux
        # Exemple :
        # {
        #   "cow": 5,
        #   "sheep": 2
        # }
        self.animals = {}


    # ==========================================
    # Méthode pour ajouter des animaux
    # ==========================================
    def add_animal(self, animal_type=None, count=1, **kwargs):

        # ------------------------------------------
        # Cas 1 : ajout classique
        # Exemple :
        # add_animal("cow", 5)
        # ------------------------------------------
        if animal_type:

            # Vérifie si l'animal existe déjà
            if animal_type in self.animals:

                # Ajouter la quantité
                self.animals[animal_type] += count

            else:
                # Créer une nouvelle entrée
                self.animals[animal_type] = count


        # ------------------------------------------
        # Cas 2 : ajout multiple avec **kwargs
        # Exemple :
        # add_animal(cow=5, sheep=2, goat=12)
        # ------------------------------------------
        for animal, qty in kwargs.items():

            # Vérifier si l'animal existe déjà
            if animal in self.animals:

                # Ajouter la quantité
                self.animals[animal] += qty

            else:
                # Ajouter l'animal
                self.animals[animal] = qty


    # ==========================================
    # Méthode pour afficher les informations
    # ==========================================
    def get_info(self):

        # Début du texte
        info = f"{self.name}'s farm\n\n"

        # Parcourir les animaux
        for animal, count in self.animals.items():

            # Ajouter chaque animal au texte
            info += f"{animal:<10} : {count}\n"

        # Ajouter la phrase finale
        info += "\n\tE-I-E-I-0!"

        # Retourner le texte
        return info


    # ==========================================
    # Méthode pour retourner les types d'animaux
    # ==========================================
    def get_animal_types(self):

        # Retourner les clés triées
        return sorted(self.animals.keys())


    # ==========================================
    # Méthode courte d'information
    # ==========================================
    def get_short_info(self):

        # Liste des animaux triés
        animal_list = []

        # Parcourir les animaux
        for animal in self.get_animal_types():

            # Ajouter "s" si le nombre > 1
            if self.animals[animal] > 1:
                animal_list.append(animal + "s")

            else:
                animal_list.append(animal)

        # Construire la phrase finale
        sentence = ", ".join(animal_list[:-1])

        # Ajouter le dernier animal avec "and"
        if len(animal_list) > 1:
            sentence += " and " + animal_list[-1]

        elif len(animal_list) == 1:
            sentence = animal_list[0]

        # Retourner la phrase
        return f"{self.name}'s farm has {sentence}."


# ==========================================
# TEST DU PROGRAMME
# ==========================================

# Création de la ferme
macdonald = Farm("McDonald")


# ==========================================
# Ajouter des animaux (méthode classique)
# ==========================================

macdonald.add_animal('cow', 5)

# sheep sans quantité = 1 par défaut
macdonald.add_animal('sheep')

# Ajouter encore un sheep
macdonald.add_animal('sheep')

# Ajouter des goats
macdonald.add_animal('goat', 12)


# ==========================================
# Affichage des informations
# ==========================================

print(macdonald.get_info())


# ==========================================
# Affichage des types d'animaux
# ==========================================

print("\nListe triée des animaux :")
print(macdonald.get_animal_types())


# ==========================================
# Affichage version courte
# ==========================================

print("\nVersion courte :")
print(macdonald.get_short_info())


# ==========================================
# BONUS : Ajouter plusieurs animaux
# ==========================================

macdonald.add_animal(
    horse=3,
    chicken=7,
    duck=4
)

print("\n=== Après ajout multiple ===")
print(macdonald.get_info())