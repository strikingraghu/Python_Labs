"""
    In general, statements are executed sequentially.
    The first statement in a function is executed first, followed by the second, and so on.
    There may be a situation when you need to execute a block of code several number of times.
    Programming languages provide various control structures that allow for more complicated execution paths.
    Loop Type & Description
        WHILE LOOP
            Repeats a statement or group of statements while a given condition is TRUE.
            It tests the condition before executing the loop body.
        FOR LOOP
            Executes a sequence of statements multiple times and abbreviates the code that manages the loop variable.
        NESTED LOOP
            You can use one or more loop inside any another while loop, for loop or do..while loop.
"""

# While Loop
print("# While Loop in Python programming")
simple_count = 0
while simple_count < 10:
    simple_count += 1
    print("Loop Executed =", simple_count)
print("Good bye!")
print()

# While Loop + Else + If
print("# While Loop in Python programming")
another_count = 0
while another_count <= 10:
    another_count += 1
    print("In the while loop section =", another_count)
else:
    if another_count == 10:
        print("Execution completes now!")
print("Good bye!")
print()

# Takes user's input
print("# Takes user's input in Python programming")
user_input = input("Enter the number =")
print(user_input.__class__)
if type(user_input.__class__ == int):
    print("It's a valid entry")
elif type(user_input.__class__ == str):
    print("It's a string value")
elif type(user_input.__class__ == complex):
    print("It's a complex value")
else:
    print("Please enter a valid entry!")
print()

# For Loop (Is this a Prime number?)
print("# For Loop (Is this a Prime number?) in Python programming")
for num in range(10, 20):
    for i in range(2, num):
        if num % i == 0:
            j = num / i
            print('%d equals %d * %d' % (num, i, j))
            break
    else:
        print(num, 'is a prime number')
print("Good Bye!")
print()
