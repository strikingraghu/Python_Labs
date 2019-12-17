"""Keywords are the reserved words in Python.
We cannot use a keyword as a variable name, function name or any other identifier.
They are used to define the syntax and structure of the Python language.
In Python, keywords are case sensitive.
There are 33 keywords in Python 3.7. This number can vary slightly in the course of time."""


# Python code to demonstrate keywords

x = None
y = None
print("x == y?", x == y)
print("None == 0?", None == 0)
print("None == 1?", None == 1)
print(True or False)
print(False or True)
print(not True)

# Python code to demonstrate del

list_1 = [100, 200, 300]
print("List elements before deletion =", list_1)
del(list_1[0])
print("List elements after deletion =", list_1)

# Python code to explain assert

list_2 = [5, 6, 7, 8, 9, 10]
print("Assert keyword example =", 7 < 5)
assert(7 < 5)

# Python code to demonstrate working of in and is

sample_string = "geeksforgeeks"
sub_string = "geek"
if sub_string in sample_string:
    print("Yes, geeks is available in geeksforgeeks")
else:
    print("No")

print(" " is " ")  # using is to check object identity string is immutable hence occupy same memory location
print([] is [])  # using is to check object identity dictionary is mutable hence occupy different memory location

# Python code to demonstrate working of global keyword

one_string = 10


# printing one_string
def read():
    print("Value without any modifications =", one_string)


def modification_1():
    global one_string
    one_string = 5


def modification_2():
    one_string = 15


read()
modification_1()
read()
modification_2()
read()

# Python code to demonstrate working of non local keyword
print("Value of a using nonlocal is : ", end="")


def outer_one():
    sample_a = 5

    def inner_one():
        nonlocal sample_a
        sample_a = 10
    inner_one()
    print(sample_a)


outer_one()


print("Value of a without nonlocal is :", end="")


def outer_two():
    another_sample_a = 5

    def inner_two():
        another_sample_a = 10
    inner_two()
    print(another_sample_a)


outer_two()
