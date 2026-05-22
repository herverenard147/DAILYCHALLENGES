# Exercice 1 : Chats

# Instructions :

# Utilisez la classe fournie pour créer trois objets chat. Ensuite, créez une fonction pour trouver le chat le plus âgé et imprimez ses détails.Cat


class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age   

# Step 1: Create cat objects
cat1 = Cat("cat1", 10)
cat2 = Cat("cat2", 5)
cat3 = Cat("cat3", 15)

# Step 2: Create a function to find the oldest cat
def find_oldest_cat(cat1, cat2, cat3):
    oldest_cat = max(cat1, cat2, cat3, key=lambda cat: cat.age)
    return oldest_cat

# Step 3: Print the oldest cat's details
oldest_cat = find_oldest_cat(cat1, cat2, cat3)
print(f"The oldest cat is {oldest_cat.name} and it is {oldest_cat.age} years old.")



# Exercice 2 : Chiens
# But : Créez une classe, instanciez des objets, appelez des méthodes et comparez les tailles des chiens.Dog


# Instructions :

# Créez une classe avec des méthodes pour aboyer et sauter. Instanciez des objets pour chiens, appelez leurs méthodes et comparez leurs tailles.Dog

class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        print(f"{self.name} jumps {self.height * 2} cm high!")

# Step 2: Create dog objects
davids_dog = Dog("Rex", 50)
sarahs_dog = Dog("Bella", 40)

# Step 3: Print dog details and call methods
print(f"{davids_dog.name} is {davids_dog.height} cm tall.")
davids_dog.bark()
davids_dog.jump()

print(f"{sarahs_dog.name} is {sarahs_dog.height} cm tall.")
sarahs_dog.bark()
sarahs_dog.jump()

# Step 4: Compare dog heights
if davids_dog.height > sarahs_dog.height:
    print(f"{davids_dog.name} is bigger than {sarahs_dog.name}.")
else:
    print(f"{sarahs_dog.name} is bigger than {davids_dog.name}.")

#  Exercice 3 : Qui est le producteur de la chanson ?
# But : Créez une classe pour représenter les paroles des chansons et imprimez-les.Song

# Instructions :

# Créez un cours avec une méthode pour imprimer les paroles des chansons ligne par ligne.Song

class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line) 
stairway = Song(["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"])
stairway.sing_me_a_song()   



# Exercice 4 : Après-midi au zoo
# But :

# Créez une classe pour gérer les animaux. Le cours devrait permettre d’ajouter des animaux, de les exposer, de les vendre et de les organiser en groupes alphabétiques.Zoo



class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
        else:
            print(f"{new_animal} is already in the zoo.")

    def get_animals(self):
        print(self.animals)

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
        else:
            print(f"{animal_sold} is not in the zoo.")

    def sort_animals(self):  # sort alphabetically
        sorted_animals = sorted(self.animals)
        groups = {}
        for animal in sorted_animals:
            first_letter = animal[0]
            if first_letter not in groups:
                groups[first_letter] = [animal]
            else:
                groups[first_letter].append(animal)
        return groups    

    def get_groups(self):   
        groups = self.sort_animals()
        for group in groups:
            print(f"{group}: {groups[group]}")  
# Step 2: Create a Zoo instance
brooklyn_safari = Zoo("Brooklyn Safari")

# Step 3: Use the Zoo methods
brooklyn_safari.add_animal("Giraffe")
brooklyn_safari.add_animal("Bear")
brooklyn_safari.add_animal("Baboon")
brooklyn_safari.get_animals()
brooklyn_safari.sell_animal("Bear")
brooklyn_safari.get_animals()
brooklyn_safari.sort_animals()
brooklyn_safari.get_groups()    


# Bonus : Modifie la méthode pour obtenir que vous n’ayez pas à la répéter à chaque fois pour un nouvel animal, vous pouvez passer plusieurs noms d’animaux séparés par une virgule.add_animal()*args
def add_animal(self, *new_animals):   
    for new_animal in new_animals:    
        if new_animal not in self.animals:
            self.animals.append(new_animal)
        else:
            print(f"{new_animal} is already in the zoo.")