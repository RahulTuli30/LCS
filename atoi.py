class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        
        if len(str) == 0:
            return 0
        
        sign = 1
        
        if str[0] in ['+', '-']:
            # print("Hola")
            if str[0] == '-':
                # print("Hola22")
                
                sign = -1
            
            str = str[1:]
        
        if not str:
            return 0
        
        if not str[0].isdigit():
            return 0
        
        result = 0
        for i, c in enumerate(str):
            if not c.isdigit():
                result = int(str[0: i]) * sign
                break
        else:
            result = int(str) * sign
        
        if result >= 2 ** 31:
            return 2 ** 31-1
        
        if result < -2 ** 31:
            return -2 ** 31
        
        return result
        
