"""
Calculate the sum of all numbers from 1 to N
"""

num = int(input("enter the total number to find sum "))
sum_num = 0
for i in range(1, num+1):
    sum_num = sum_num + i

print(sum_num)