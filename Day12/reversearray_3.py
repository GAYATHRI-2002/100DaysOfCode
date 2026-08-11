#Reverse a given array

arr = [1, 2, 3, 4, 5]
 
p1 = 0
p2 = len(arr) - 1
 
for i in arr:
    if p1 < p2: 
        arr[p1], arr[p2] = arr[p2], arr[p1]
        p1 += 1
        p2 -= 1
    
print("the reversed array: ", arr)
        
         
