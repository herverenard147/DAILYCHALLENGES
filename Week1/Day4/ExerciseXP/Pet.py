
class Pets:
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat:
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'


class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'


# Étape 1 : Créer la classe Siamese
class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'


# Étape 2 : Liste d'instances de chats
bengal    = Bengal("Leo", 3)
chartreux = Chartreux("Luna", 5)
siamese   = Siamese("Mia", 2)

all_cats = [bengal, chartreux, siamese]

# Étape 3 : Créer une instance de Pets
sara_pets = Pets(all_cats)

# Étape 4 : Promener les chats
sara_pets.walk()
