"""
Write a Python function that accepts two integer numbers. If the product of the two numbers is less than or equal to 1000,
 return their product; otherwise, return their sum.
"""

def function_sum(num1, num2):

    product = num1 * num2

    if product <= 1000:
        return product
    else:
        return num1 + num2
num1, num2 = map(int, input("enter two integers: ").split())
result = function_sum(num1, num2)
print("The result is ", result )