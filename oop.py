# Object Oriented Programming 

# Class

class Person():
    def __init__(self, name, height, weight, color):
        self.height = height
        self.weight = weight
        self.color = color
        self.name = name

    def stand(self):
        print(self.name)
        print("This person is now standing")

    def sit(self):
        print(self.name)
        print("This person is now sitting")
    
    def run(self):
        print(self.name)
        print("This person is now running")

Person1 = Person("Person 1", "180cm", "80kg", "black" )

Person2 = Person("Person 2", "175cm", "78kg", "Caramel")

print(f"The person1 height is {Person1.height}")
print(f"The person2 height is {Person2.height}")

Person1.sit()
Person2.stand()


    