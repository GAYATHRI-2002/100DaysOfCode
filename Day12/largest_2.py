# Given an array, we have to find the largest element in the array.

arr1 = [0,34,2,34,344,3,5,66,1000]

max = arr1[0]

for i in range(0, len(arr1)):
    if arr1[i] > max:
        max = arr1[i]
        
print("The largest element is ",max)
