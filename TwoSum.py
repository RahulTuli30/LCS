"""
This file contains the solution to LeetCode TwoSum problem
Difficulty Level : Easy
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:        
        ordered_complements = {}
        
        for i, number in enumerate(nums):
            
            if i != 0 and number in ordered_complements:
                return [ordered_complements[number], i]
            else:
                ordered_complements[target - number] = i
        
        return []
            
