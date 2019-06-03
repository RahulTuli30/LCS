"""
This file contains solution to LONGEST SUBSTRING WITHOUT REPEATING CHARACTERS 
problem in LeetCode

Difficulty : Medium
Link : https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) in (0, 1):
            return len(s)
        
        max_len = 0
        counter_dict = {}
        start, end =0, 0
        
        for i, character in enumerate(s):
            if character in counter_dict:
                tmp_len = end - start
                
                if tmp_len > max_len:
                    max_len  = tmp_len
                
                new_start = counter_dict[character] + 1
                
                for c2 in iter(s[start : new_start]):
                    del counter_dict[c2]
                
                start = new_start
                
            
            counter_dict[character] = i
            end +=1
            
        return end - start if end - start > max_len else max_len 
            
        
   
