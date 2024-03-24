from math import *

def calculate(expression):
    try:
        # Evaluate the expression and return the result
        result = eval(expression)
        return result
    except Exception as e:
        return "Error in calculation: " + str(e)

# Input from user
user_input = input("Enter your math operation: ")
result = calculate(user_input)
print(f"Result: {result}")
