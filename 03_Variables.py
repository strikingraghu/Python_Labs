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
print("Display String's 4 Character =", string_1[4])
print("Display String's between 2 & 4 =", string_2[2:4])
print("Display String's =", string_2[:4])
print("Display String's =", string_2[2:])
print("Display String's =", string_2[:])
print()

# Lists
print("# Lists in Python code")
list_1 = [22, "Ram", 339273.223, 3778.99271j, "Suresh"]
print("Index value of String =", list_1.index("Suresh"))
list_1.append("Apple")
print("List values after appending an element =", list_1)
list_2 = list_1.copy()
print("List_2 values after copying it via List_1 =", list_2)
list_2.reverse()
print("Reversing List_1 in this context =", list_2)
print()

# Tuple
print("# Tuple in Python code")
tuple_1 = (34, 389, "Ram", "Suresh", 9095920489.376251j)
print("Length of Tuple in this code =", tuple_1.__len__())
print("Class of the Tuple in this code =", tuple_1.__class__)
print("Hash value of Tuple in this code =", tuple_1.__hash__())
print("Is element present =", tuple_1.__contains__("Ram"))
print()

# Sets
print("# Sets in Python code")
set_1 = {33, "Ram", 2910, "Suresh", 588.901838, 48199201.382J, "Hemanth"}
print("Printing all elements of Set_1 without duplicates = ", set_1)
print("Length of Set_1 =", set_1.__len__())
set_2 = set_1.copy()
print("Set_2 values by copying Set_1 elements =", set_2)
set_2.add(100)
print("Difference between 2 sets =", set_2.difference(set_1))
print("Subset values between both the sets =", set_1.issubset(set_2))
print("Set_2 class details =", set_2.__class__)
print("Size of Set_2 in this code =", set_2.__sizeof__())
print()

# Dictionary
print("# Dictionary in Python code")
dict_1 = {1: "apple", "b": "boy", 2: "car", "c": 4, "d": 83, "e": 83}
print("Displaying only keys within the dictionary =", dict_1.keys())
print("Displaying only values within the dictionary =", dict_1.values())
print("Getting value for key 'c' =", dict_1.get("c"))
print()
