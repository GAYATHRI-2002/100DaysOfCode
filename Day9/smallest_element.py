""" Find the smallest element in an array
Example 1:
Input:
 arr[] = {2, 5, 1, 3, 0}
Output:
 0
Explanation:
  0 is the smallest element in the array.

Example 2:
Input:
 arr[] = {8, 10, 5, 7, 9}
Output:
 5
Explanation:
  5 is the smallest element in the array."""

#brute force
arr = [8, 10, 5, 7, 9]
arr.sort() #arr is modified permanently
print(arr[0])
arr = sorted(arr) #array is not getting modified
print(arr[0])

arr = [2, 5, 1, 3, 0]
minimum = arr[0]

for i in arr:
    if i < minimum:
        minimum = i

print("The smallest element is ",minimum)

