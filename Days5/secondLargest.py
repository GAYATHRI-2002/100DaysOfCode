def secondLargestnum(arr):
    largest = -1
    secondLargest = -1

    for i in arr:
        if i > largest:
            secondLargest = largest
            largest = i
        elif i < largest and i > secondLargest:
            secondLargest = i

    return secondLargest

arr = [22,12,11,43,8,2,54]
result = secondLargestnum(arr)
print(result)