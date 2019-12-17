"""A namespace is a system to have a unique name for each and every object in Python.
An object might be a variable or a method. Python itself maintains a namespace in the form of a Python dictionary.
Let’s go through an example, a directory-file system structure in computers."""


# Variables in Global & Local namespace
def outer_func():
    variable_a = 20

    def inner_func():
        variable_a = 30
        print("1 - variable_a =", variable_a)
    inner_func()
    print("2 - variable_a =", variable_a)


variable_a = 10
outer_func()
print("3 - variable_a =", variable_a)


# Variables in Global & Local namespace


def outer_func():
    global variable_a
    variable_a = 20

    def inner_func():
        global variable_a
        variable_a = 30
        print("1 - variable_a =", variable_a)

    inner_func()
    print("2 - variable_a =", variable_a)


variable_a = 10
outer_func()
print("3 - variable_a =", variable_a)
