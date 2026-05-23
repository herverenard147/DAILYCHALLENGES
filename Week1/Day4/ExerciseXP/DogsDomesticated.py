
import random

# (importer Dog depuis l'exercice 2 dans un vrai projet)

class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *args):
        names = [self.name] + [dog.name for dog in args]
        print(f"{', '.join(names)} all play together")

    def do_a_trick(self):
        if self.trained:
            tricks = [
                "does a barrel roll",
                "stands on his back legs",
                "shakes your hand",
                "plays dead"
            ]
            print(f"{self.name} {random.choice(tricks)}")
        else:
            print(f"{self.name} is not trained yet!")


# Test
my_dog  = PetDog("Fido", 2, 10)
dog_b   = PetDog("Buddy", 3, 15)
dog_c   = PetDog("Max",   4, 20)

my_dog.train()
my_dog.play(dog_b, dog_c)
my_dog.do_a_trick()

# Étape 4 


class Person:
    def __init__(self, first_name, age):
        self.first_name = first_name
        self.age = age
        self.last_name = ""

    def is_18(self):
        return self.age >= 18


class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = []

    def born(self, first_name, age):
        person = Person(first_name, age)
        person.last_name = self.last_name
        self.members.append(person)

    def check_majority(self, first_name):
        for member in self.members:
            if member.first_name == first_name:
                if member.is_18():
                    print(
                        "You are over 18, your parents Jane and John "
                        "accept that you will go out with your friends"
                    )
                else:
                    print("Sorry, you are not allowed to go out with your friends.")
                return
        print(f"{first_name} is not a member of this family.")

    def family_presentation(self):
        print(f"Family: {self.last_name}")
        for member in self.members:
            print(f"  - {member.first_name}, age {member.age}")


# Test
my_family = Family("Smith")
my_family.born("Alice", 20)
my_family.born("Bob",   15)
my_family.born("Clara", 18)

my_family.family_presentation()
my_family.check_majority("Alice")
my_family.check_majority("Bob")
my_family.check_majority("Clara")