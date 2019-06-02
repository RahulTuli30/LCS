"""
Solution to LeetCode problem Add Two Numbers
Difficulty : Medium
Link : https://leetcode.com/problems/add-two-numbers/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        flag1 , flag2= l1 is not None, l2 is not None
        
        l3 = None
        head = None
        carry = 0
        
        while (flag1 and flag2):
            s = l1.val + l2.val + carry
            carry = s // 10
            s = s % 10
            
            if not l3:
                l3 = ListNode(s)
                head = l3
            else:
                l3.next = ListNode(s)
                l3 = l3.next
            
            l1 = l1.next
            l2 = l2.next
            
            flag1 = l1 is not None
            flag2 = l2 is not None
        
