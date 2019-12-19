"""Keywords are the reserved words in Python.
We cannot use a keyword as a variable name, function name or any other identifier.
They are used to define the syntax and structure of the Python language.
In Python, keywords are case sensitive.
There are 33 keywords in Python 3.7. This number can vary slightly in the course of time."""

import keyword

# Python code to demonstrate keywords
print("# Python code to demonstrate keywords")

x = None
y = None
print("x == y?", x == y)
print("None == 0?", None == 0)
print("None == 1?", None == 1)
print(True or False)
print(False or True)
print(not True)
print()

# Python code to demonstrate del
print("# Python code to demonstrate del")

list_1 = [100, 200, 300]
print("List elements before deletion =", list_1)
del(list_1[0])
print("List elements after deletion =", list_1)
print()

# Python code to explain assert
print("# Python code to explain assert")

list_2 = [5, 6, 7, 8, 9, 10]
print("Assert keyword example =", 7 < 5)
#assert(7 < 5)
print()

# Python code to demonstrate working of in and is
print("# Python code to demonstrate working of in and is")

sample_string = "geeksforgeeks"
sub_string = "geek"
if sub_string in sample_string:
    print("Yes, geeks is available in geeksforgeeks")
else:
    print("No")

print(" " is " ")  # using is to check object identity string is immutable hence occupy same memory location
print([] is [])  # using is to check object identity dictionary is mutable hence occupy different memory location
print()

# Python code to demonstrate working of global keyword
print("# Python code to demonstrate working of global keyword")

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
print()

# Python code to demonstrate working of non local keyword
print("# Python code to demonstrate working of non local keyword")
print("Value of a using nonlocal is : ", end="")


def outer_one():
    sample_a = 5

    def inner_one():
        nonlocal sample_a
        sample_a = 10
    inner_one()
    print(sample_a)


outer_one()
print()

# Python code to demonstrate without use of non local keyword
print("# Python code to demonstrate without non local keyword")

print("Value of a without nonlocal is :", end="")


def outer_two():
    another_sample_a = 5

    def inner_two():
        another_sample_a = 10
    inner_two()
    print(another_sample_a)


outer_two()
print()

# Python code to to check if a string is a valid keyword
print("Python code to to check if a string is a valid keyword")

s1 = "geeks"
s2 = "for"
s3 = "else"
s4 = "elif"
s5 = "break"
s6 = "try"
s7 = "assert"

if keyword.iskeyword(s1):
    print("S1 is a keyword - ", s1)
else:
    print("S1 is not a keyword -", s1)

if keyword.iskeyword(s2):
    print("S2 is a keyword - ", s2)
else:
    print("S2 is not a keyword -", s2)

if keyword.iskeyword(s3):
    print("S3 is a keyword - ", s3)
else:
    print("S3 is not a keyword -", s3)

if keyword.iskeyword(s4):
    print("S4 is a keyword - ", s4)
else:
    print("S4 is not a keyword -", s4)

if keyword.iskeyword(s5):
    print("S5 is a keyword - ", s5)
else:
    print("S5 is not a keyword -", s5)

if keyword.iskeyword(s6):
    print("S6 is a keyword - ", s6)
else:
    print("S6 is not a keyword -", s6)

if keyword.iskeyword(s7):
    print("S7 is a keyword - ", s7)
else:
    print("S7 is not a keyword -", s7)
