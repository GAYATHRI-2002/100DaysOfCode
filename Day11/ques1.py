#1.Find the smallest element in an array

def smallest_element():
    smallest = arr[0]

    for i in range(0, len(arr)) :
        if arr[i] < smallest:
            smallest = arr[i]
    return smallest




arr= [2, 5, 1, 3, 6]
result = smallest_element()
print("the smallest element is ", result )
