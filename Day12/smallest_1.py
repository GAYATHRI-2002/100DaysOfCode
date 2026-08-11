#Given an array, we have to find the smallest element in the array.

arr1 = [33,21,43,15,112,24,3]

min = arr1[0]

for i in range(0, len(arr1)):
    if arr1[i] < min:
        min = arr1[i]
    

print("the smallest element is ",arr1[i])
