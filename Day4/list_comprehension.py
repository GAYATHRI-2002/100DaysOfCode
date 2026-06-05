"""
Write a single-line list comprehension that takes a list of strings,
filters out strings shorter than 4 characters, and
 converts the remaining strings to uppercase.
"""
list1 = input("enter the list seperated by comma ").split(",")
string_remain = [i.upper() for i in list1 if len(i) >= 4 ]
print(",".join(string_remain))