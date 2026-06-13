"""
 Write a program to check if a user-entered string contains any numeric digits.
  Use a for loop to examine each character
"""
input_string = "Python3"
is_number = False
for i in input_string:
    if i.isdigit():
        is_number = True
        break

print(f"There is a number in {input_string} is  {is_number}")