# Création de la classe Zoo
class Zoo:

    # Constructeur
    def __init__(self, zoo_name):

        # Nom du zoo
        self.zoo_name = zoo_name

        # Liste vide pour stocker les animaux
        self.animals = []

        # Dictionnaire pour les groupes
        self.groups = {}


    # =========================
    # Ajouter un ou plusieurs animaux
    # =========================
    def add_animal(self, *new_animals):

        # Boucle sur tous les animaux reçus
        for animal in new_animals:

            # Vérifier si l'animal existe déjà
            if animal not in self.animals:

                # Ajouter l'animal
                self.animals.append(animal)

            else:
                print(f"{animal} existe déjà dans le zoo.")


    # =========================
    # Afficher les animaux
    # =========================
    def get_animals(self):

        print(f"\nAnimaux du zoo {self.zoo_name} :")

        for animal in self.animals:
            print(animal)


    # =========================
    # Vendre un animal
    # =========================
    def sell_animal(self, animal_sold):

        # Vérifier si l'animal existe
        if animal_sold in self.animals:

            # Supprimer l'animal
            self.animals.remove(animal_sold)

            print(f"{animal_sold} a été vendu.")

        else:
            print(f"{animal_sold} n'existe pas dans le zoo.")


    # =========================
    # Trier et regrouper les animaux
    # =========================
    def sort_animals(self):

        # Trier la liste alphabétiquement
        sorted_animals = sorted(self.animals)

        # Dictionnaire vide
        grouped = {}

        # Parcourir les animaux triés
        for animal in sorted_animals:

            # Première lettre
            first_letter = animal[0]

            # Si la lettre n'existe pas encore
            if first_letter not in grouped:

                # Créer une nouvelle liste
                grouped[first_letter] = []

            # Ajouter l'animal dans le groupe
            grouped[first_letter].append(animal)

        # Sauvegarder dans l'attribut groups
        self.groups = grouped

        return grouped


    # =========================
    # Afficher les groupes
    # =========================
    def get_groups(self):

        print("\nGroupes d'animaux :")

        for letter, animals in self.groups.items():
            print(f"{letter}: {animals}")


# =========================
# Étape 2 : Création du zoo
# =========================

brooklyn_safari = Zoo("Brooklyn Safari")


# =========================
# Étape 3 : Utilisation des méthodes
# =========================

# Ajouter des animaux
brooklyn_safari.add_animal(
    "Giraffe",
    "Bear",
    "Baboon",
    "Lion",
    "Zebra",
    "Cat",
    "Cougar"
)

# Afficher les animaux
brooklyn_safari.get_animals()

# Vendre un animal
brooklyn_safari.sell_animal("Bear")

# Réafficher les animaux
brooklyn_safari.get_animals()

# Trier et regrouper
brooklyn_safari.sort_animals()

# Afficher les groupes
brooklyn_safari.get_groups()