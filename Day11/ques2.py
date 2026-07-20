#Given an array of integers nums, return the value of the largest element in the array
class Solution:
    def largestElement(self, nums):

        large = nums[0]
        
        for i in nums:
            if i > large:
                large = i
        return large    
            
