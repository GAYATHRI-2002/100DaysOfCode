"""
 Count occurrences of a specific element in a list
"""
list1 = [4,5,3,1,2,5,5]
count = 0
target  = int(input("enter the item "))
for i in list1:
    if i == target:
        count += 1
print(f"count of {target} ",count)

