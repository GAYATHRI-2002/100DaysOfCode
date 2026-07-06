"""
Given an array of integers nums, return the value of the largest element in the array
Example 1
Input: nums = [3, 3, 6, 1]
Output: 6
Explanation: The largest element in array is 6
"""

nums = [3, 3, 6, 1]
class Solution:
    def largestElement(self, nums):

        large = nums[0]

        for i in nums:
            if i > large:
                large = i
        return large

