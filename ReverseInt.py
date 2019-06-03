class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = int(str(abs(x))[::-1])
        
        result *= 1 if x >= 0 else -1
        return 0 if result >= 2 ** 31 or result < -2 ** 31 else result 
