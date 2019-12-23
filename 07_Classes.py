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
