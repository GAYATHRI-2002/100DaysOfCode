#Given an array of integers nums, return the second-largest element in the array. If the second-largest element does not exist, return -1.
class Solution:
    def secondLargestElement(self, nums):
        large = -float('inf')
        slarge = -float('inf')
        for i in nums:
            if i > large:
                slarge = large
                large = i
            elif i < large and i > slarge:
                slarge = i
        return slarge if slarge != -float('inf') else -1


        
