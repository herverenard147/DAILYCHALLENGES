class Farm:
    """A class to represent a farm."""

    def __init__(self, farm_name):
        """Initialize a new Farm instance."""
        self.name = farm_name
        self.animals = {}

    def add_animal(self, animal_type, count=1):
        """Add or update an animal count in the farm."""
        if animal_type in self.animals:
            self.animals[animal_type] += count
        else:
            self.animals[animal_type] = count

    def get_info(self):
        """Return a formatted string with farm name, animals and their counts."""
        info = f"{self.name}'s farm\n\n"
        for animal, count in self.animals.items():
            info += f"{animal} : {count}\n"
        info += "\n    E-I-E-I-0!"
        return info

    def get_animal_types(self):
        """Return a sorted list of all animal types."""
        return sorted(self.animals.keys())

    def get_short_info(self):
        """Return a short string summarizing the farm's animals."""
        animal_types = self.get_animal_types()
        animal_list = []
        for animal in animal_types:
            if self.animals[animal] > 1:
                animal_list.append(animal + "s")
            else:
                animal_list.append(animal)
        return f"{self.name}'s farm has {', '.join(animal_list)}."


def main():
    """Main function to test the Farm class."""
    macdonald = Farm("McDonald")
    macdonald.add_animal('cow', 5)
    macdonald.add_animal('sheep')
    macdonald.add_animal('sheep')
    macdonald.add_animal('goat', 12)
    print(macdonald.get_info())
    print(macdonald.get_animal_types())
    print(macdonald.get_short_info())


if __name__ == "__main__":
    main()