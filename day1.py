print("Hello world")

#reverse an array

def revArray(arr1):
    n = len(arr1)
    temp1 = [0] * n

    for i in range(n):
        temp1[i] =  arr1[n-i-1]
    return temp1

arr1 = [12,34,1,4,6,43,10]
rev_array = revArray(arr1)
print("The original array is :", arr1)
print("The reversed array is: ", rev_array)

#using two pointers

def revArray(arr1):
    left = 0
    right = len(arr1) - 1

    while left < right:
        arr1[left], arr1[right] = arr1[right], arr1[left]
        left += 1
        right -= 1
    return arr1


arr1 = [3,2,11,45,22,16] 
print("The original array is :", arr1) 
rev_array = revArray(arr1)
print("The reversed array is: ", rev_array)

#by swapping elements

def revArray(arr1):
    n = len(arr1)

    for i in range(n//2):
        temp = arr1[i]
        arr1[i] = arr1[n-i-1]
        arr1[n-i-1] = temp
    return arr1

arr1 = [22,12,232,454,2,1]
print("The given array : ",arr1)
rev_array = revArray(arr1)
print("The reversed array :",arr1)
