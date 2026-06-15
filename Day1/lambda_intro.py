"""Add 10 to argument a, and return the result:"""
x = lambda a: a + 10
print(x(4))
"""Multiply argument a with argument b and return the result:"""
res = lambda a, b : a * b
print(res(2,3))
"""convert to upper case"""
s1 = "welcome home"
s2 = lambda s1: s1.upper()
print(s2(s1))