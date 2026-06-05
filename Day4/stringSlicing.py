"""
Write a function to remove characters from a string starting from index 0 up to n and return a new string.
"""
def string_remove(string1, n):
    new_string = []
    for i in range(n, len(string1)):
        new_string.append(string1[i])
    return new_string

string1 = input("Enter a string: ")
char_remove = int(input("Enter the number of character need to remove from the string: "))
print(string_remove(string1,char_remove))