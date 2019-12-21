"""
    Operators are the constructs which can manipulate the value of operands.
    Consider the expression 4 + 5 = 9. Here, 4 and 5 are called operands and + is called operator.
    Types of Operator:
        Python language supports the following types of operators.
            Arithmetic Operators
            Comparison (Relational) Operators
            Assignment Operators
            Bitwise Operators
            Membership Operators
            Identity Operators
            Operators Precedence
"""

# Example - Python Arithmetic Operators
# Assume variable A holds 10 and variable B holds 20, then −

# Python code for Generic operators
print("# Python code for Arithmetic operations")
var_a = 10
var_b = 20
var_c = var_a + var_b
print("Addition =", var_a + var_b)
print("Subtraction =", var_b - var_a)
print("Multiplication =", var_a * var_b)
print("& Binary AND =", var_a & var_b)
print("| Binary OR =", var_a | var_b)
print("^ Binary XOR =", var_a ^ var_b)
print("~ Ones Complement =", ~var_b)
print("<< Binary Left Shift =", var_a << 2)
print(">> Binary Right Shift =", var_a >> 2)
var_c = 20
var_c *= var_a
print("Value of var_c after modifications =", var_c)
