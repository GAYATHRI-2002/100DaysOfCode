"""
Iterate through the first 10 numbers (0–9).
 In each iteration, print the current number, the previous number, and their sum.
"""

def cumulative_iteration(max_num):
    previous_num = 0
    for i in range(max_num):
        sum_pre = i + previous_num
        print(f"current number {i}, the previous number {previous_num}, and their sum {sum_pre}")
        previous_num = i

num = int(input("Enter the number to find the previous and current and their sum : "))
cumulative_iteration(num)