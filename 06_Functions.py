"""
    In Python, function is a group of related statements that perform a specific task.
    Functions help break our program into smaller and modular chunks.
    As our program grows larger and larger, functions make it more organized and manageable.
    Furthermore, it avoids repetition and makes code reusable.
"""

# Sample Function
print("# Sample function in Python code")


def odd_even(number):
    if number % 2 == 0:
        print(number, "= Number is even!")
    else:
        print(number, "= Number is odd!")


simple_range = range(1, 5)
print("Printing values of simple_range =", simple_range)
for each_element in simple_range:
    odd_even(each_element)
print("Iteration done!")
print()

# Sample Function
print("# Sample function in Python code")


def calculate_factorial(x):
    if x == 1:
        return 1
    else:
        return x * calculate_factorial(x-1)


testing_value = 5
print("Factorial values =", calculate_factorial(testing_value))  # 5 x 4 x 3 x 2 x 1
print()
