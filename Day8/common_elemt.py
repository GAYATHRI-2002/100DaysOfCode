"""
 Take two lists and find the elements that appear in both.
  Use Sets to perform the operation.
"""
list_a = [1, 2, 3, 4, 5]
list_b = [4, 5, 6, 7, 8]

common_list = []

for i in list_a:
    if i in list_b:
        common_list.append(i)

print("Common elements in list: ", common_list)