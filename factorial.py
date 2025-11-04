# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)    
# n = 3
# print(factorial(n))

import math
try:
    print(math.factorial(-5))
except ValueError:
    print("Value not defined")