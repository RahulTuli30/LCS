class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        open_paren = ['{', '(', '[']
        close_paren = ['}', ')', ']']
        
        d = dict(zip(close_paren, open_paren))
        stack = []
        for char in s:
            if char in open_paren:
                stack.append(char)
            elif not stack:
                return False
            elif d[char] == stack[len(stack)-1]:
                stack.pop()
            else:
                return False
        
        return not stack
        
