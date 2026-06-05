"""
 Display only those characters which are present at an even index number in given string.
"""
string1 = input("enter a sting or a word: ")
even_char = []
for i in range(len(string1)):
    if i % 2 == 0:
        even_char.append(string1[i])

print(even_char)



