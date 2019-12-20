"""
    Variables are nothing but reserved memory locations to store values.
    This means that when you create a variable you reserve some space in memory.
    By assigning different data types to variables, you can store integers, decimals or characters in these variables.
    Standard Data Types
        The data stored in memory can be of many types.
        Ex - A person's age is stored as a numeric value and his or her address is stored as alphanumeric characters.
        Python has various standard data types that are used to define the operations possible on them!
    Python has five standard data types −
        Numbers
        String
        List
        Tuple
        Dictionary
"""

# Assigning Values
print("# Assigning values in Python code")
counter = 100
miles = 95.33
name = "John"
print("Counter = ", counter)
print("Miles =", miles)
print("Name =", name)
print()

# Multiple Assignment
print("# Multiple Assignment")
A = B = C = 1
X, Y, Z = 10, 20, "Ram"
print("A =", A, "| B =", B, "| C =", C)
print("X =", X, "| Y =", Y, "| Z =", Z)
print()

# Numbers
print("# Numbers in Python code")
variable_1 = 25
variable_2 = 338.09
variable_3 = 6639279
variable_4 = 34.33j
print("Variable_1 Type =", type(variable_1))
print("Variable_2 Type =", type(variable_2))
print("Variable_3 Type =", type(variable_3))
print("Variable_4 Type =", type(variable_4))
print()

# Strings
print("# Strings in Python code")
string_1 = "Hello, you are in Bangalore"
string_2 = "Indeed, its a great city"
print("Length - string_1 =", len(string_1))
