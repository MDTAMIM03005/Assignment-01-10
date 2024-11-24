# Base class Animal
class Animal:
    # The __init__ method initializes the animal with a name and species
    def __init__(self, name, species):
        self.name = name
        self.species = species

    # The make_sound method returns a generic sound for the animal
    def make_sound(self):
        return "Some generic sound"

# Derived class Dog, inherits from Animal
class Dog(Animal):
    # The __init__ method calls the parent class's __init__ method to initialize name and species
    def __init__(self, name, species):
        super().__init__(name, species)

    # Override the make_sound method to return "Woof!"
    def make_sound(self):
        return "Woof!"

    # Method fetch returns a string indicating the dog is fetching a ball
    def fetch(self):
        return f"{self.name} is fetching a ball!"

# Sample input: Creating an instance of Dog class
dog = Dog("Buddy", "Golden Retriever")

# Output: Calling the make_sound method
print(dog.make_sound())  # Expected output: Woof!

# Output: Calling the fetch method
print(dog.fetch())  # Expected output: Buddy is fetching a ball!
