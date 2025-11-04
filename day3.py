#palindrome check
# def iter_palindrome(num):
#     reverse = 0

#     while num > 0:
#         digit = num % 10
#         reverse = reverse * 10 + digit
#         num = num // 10

#     if reverse == num:
#         print("it is palindrome")
#     else:
#         print("not palindrome")

# def recursive_palindrome(num, rev = 0):
#     if num == 0:
#         return rev
#     return recursive_palindrome(num //10, rev * 10 + num % 10)
# def is_palindrome(num):
#     return num == recursive_palindrome(num)

# num = 121
#iter_palindrome(num)

# recursive_palindrome(num)
# if is_palindrome(num):
#     print("It is palindrome")
# else:
#     print("Not palindrome")

# def linear_search(arr):
#     for i in range(len(arr)):
#         if arr[i] == target:
#             print(f"The {target} is in the {i} position of the array")
#             return
#     print("Not in this array")

# arr = [12,32,52,76,13]
# target = 52
# linear_search(arr)


def recursive_linear_search(arr, target, index = 0):
    if index ==len(arr):
        print("Not in this array")
        return
    
    if arr[index] == target:
        print("target is in this array")

    
    recursive_linear_search(arr, target, index+1)
