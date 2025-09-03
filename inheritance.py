class Animal:
    number_of_animals = 0

    def __init__(self, name, color):
        self.name = name
        self.color = color
        Animal.number_of_animals += 1   # shared count

    def make_sound(self):
        print(f"{self.name} is making a sound")

    def move(self):
        print(f"{self.name} is moving")

    def sleep(self):
        print(f"{self.name} is sleeping")


class Prey(Animal):
    def run_away(self):
        print(f"{self.name} is running away")


class Predator(Animal):
    """
    This ia a Predator class and it inherits from the animal class, 
    therefore,
    it has all attributes and methods/functions that the animal class already has.
    """
    def hunt(self):
        """
        This method makes an animal able to hunt
        """
        print(f"{self.name} is hunting")


# 🐄 Cow inherits Animal, but adds 'milk_production'
class Cow(Prey):
    def __init__(self, name, color, milk_production):
        super().__init__(name, color)   # inherit Animal's __init__
        self.milk_production = milk_production  # unique to cows

    def give_milk(self):
        print(f"{self.name} produces {self.milk_production} liters of milk daily.")

# 🐐 Goat inherits Animal, but adds 'horn_length'
class Goat(Prey):
    def __init__(self, name, color, horn_length):
        super().__init__(name, color)
        self.horn_length = horn_length  # unique to goats

    def show_horns(self):
        print(f"{self.name} has horns {self.horn_length} cm long.")


# 🐓 Chicken inherits Animal, but adds 'egg_count'
class Chicken(Prey):
    def __init__(self, name, color, egg_count):
        super().__init__(name, color)
        self.egg_count = egg_count  # unique to chickens

    def lay_eggs(self):
        print(f"{self.name} laid {self.egg_count} eggs today.")


class Lion (Predator):
    pass


class Snake(Predator):
    pass


class Man(Prey, Predator): 
    pass

# Create objects
cow1 = Cow("Musa", "brown", 15)
goat1 = Goat("Tunji", "black", 30)
chicken1 = Chicken("Okuko", "white", 5)
lion1 = Lion("Simba", "Brown")
snake1 = Snake("Serpent", "Green")
man1 = Man("Stephen", "Chocolate")

# Demonstrate unique + inherited behavior
print(f"The cow is {cow1.color} in color")
cow1.give_milk()      # unique
cow1.sleep()          # inherited

goat1.show_horns()    # unique
goat1.move()          # inherited

chicken1.lay_eggs()   # unique
chicken1.make_sound() # inherited

lion1.make_sound()
lion1.hunt()

snake1.sleep()

man1.hunt()
man1.run_away()

print(f"There are {Animal.number_of_animals} animals in the farm")
