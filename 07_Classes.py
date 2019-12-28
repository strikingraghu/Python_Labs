"""
    Object-oriented programming (OOP) is a programming paradigm that uses objects and their interactions to
    design applications and computer programs. There are some basic programming concepts in OOP:
        Abstraction
        Polymorphism
        Encapsulation
        Inheritance
    The abstraction is simplifying complex reality by modeling classes appropriate to the problem.
    The polymorphism is the process of using an operator or function in different ways for different data input.
    The encapsulation hides the implementation details of a class from other objects.
    The inheritance is a way to form new classes using classes that have already been defined.
"""
# Code for some sample classes, methods and instance methods


class Parrot:
    # Class Attribute
    species = "bird"

    # Instance Attribute
    def __init__(self, name, color):
        self.name = name
        self.color = color

    # Instance Method
    @staticmethod
    def sing(language):
        print("Parrot sings in " + language)
        return language


parrot_01 = Parrot("Tobi", "White")
parrot_02 = Parrot("Gobi", "Green")
print(parrot_01, parrot_02)
parrot_01.sing("English")
parrot_02.sing("Kannada")
print(parrot_01.species)
print(parrot_02.species)
print()

# Inheritance OOP's Logic
print("Inheritance is a mechanism in which one object acquires all the properties"
      "and behaviors of a parent object. ... The idea behind inheritance is that"
      "you can create new classes that are built upon existing classes."
      "When you inherit from an existing class, you can reuse methods and fields of the parent class.")
print()


class Bird:

    # Instance attribute
    def __init__(self):
        print("Bird is ready to fly!")

    def who_is_this(self):
        print("I am a bird!")

    def swim(self):
        print("Swim faster!")


class Penguin(Bird):

    def __init__(self):
        super().__init__()
        print("Penguin is now ready!")

    def who_is_this(self):
        print("Penguin")

    def swim(self):
        print("I cannot swim faster!")


peggy01 = Bird()
peggy02 = Penguin()
print()
peggy01.__init__()
peggy01.who_is_this()
peggy01.swim()
print()
peggy02.__init__()
peggy02.who_is_this()
peggy02.swim()
print("Peggy01 is calling Parent class functions and Peggy02 is calling Child class functions")
print()

# Abstraction OOP's Logic
print("Abstraction is a process of hiding the implementation details and showing"
      "only functionality to the user. Another way, it shows only essential things to the"
      "user and hides the internal details, for example, sending SMS where you type the text and send the message.")
print()


class Vehicle:

    def __init__(self, engine_type, color):
        self.engine_type = engine_type
        self.color = color
        print("Vehicle Details =", self, engine_type, color)

    @staticmethod
    def number_of_wheels(number):
        if number == 4:
            print("It's a 4 wheeler")
        if number == 2:
            print("It's a 2 wheeler")


class Bike(Vehicle):

    @staticmethod
    def bike_price():
        bike_price = 55000
        return bike_price


class Car(Vehicle):

    @staticmethod
    def car_price():
        car_price = 350000
        return car_price


print("Instantiation - Objects")
pulsar = Bike('Petrol', 'Black')
swift = Car('Diesel', 'Red')

pulsar.number_of_wheels(2)
print(pulsar.bike_price())

swift.number_of_wheels(4)
print(swift.car_price())
print()

# Encapsulation OOP's Logic
print("Encapsulation is one of the fundamental concepts in object-oriented programming (OOP)."
      "It describes the idea of bundling data and methods that work on that data within one unit,"
      "e.g., a class in Python. This concept is also often used to hide the internal representation, or"
      "state, of an object from the outside")
print()


class Computer:

    def __init__(self):
        print("Inside Computer Class")
        self._brand = 'Lenovo'

    @staticmethod
    def model():
        model = 'T440S'

    @staticmethod
    def price(price):
        price = 40000
        if price > 4000:
            print("You are planning to pay more!")
        else:
            print("You are planning to pay less!")

# Instantiation


purchase_computer = Computer()
purchase_computer.model()
purchase_computer.price(35000)  # Trying to pay 35K for this computer
print()

# Polymorphism OOP's Logic:
print("Polymorphism is the ability of an object to take on many forms."
      "The most common use of polymorphism in OOP occurs when a parent class reference"
      "is used to refer to a child class object. Any python object that can pass more "
      "than one IS-A test is considered to be polymorphic.")
print()


class Dog:

    def __init__(self):
        print("Inside Dog's Class")

    @staticmethod
    def run():
        print("Dog can run!")

# Child Class


class Labrador:

    def __init__(self):
        print("Inside Labrador's Class")

    @staticmethod
    def run():
        print("Labrador can also run!")

# Common Interface


def lets_test_running_state(any_dog):
    any_dog.run()

# Instantiation


puppy01 = Dog()
puppy02 = Labrador()
lets_test_running_state(puppy01)
lets_test_running_state(puppy02)
