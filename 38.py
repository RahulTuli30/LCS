# from collections import defaultdict
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        if n == 2:
            return "11"
        
        i = 3
        s = "11"
        
        while i <= n:
            s = self.get_next(s)
            i +=1
        
        return s
    
        # self.get_next(s)
    
    def get_next(self, last):
        
        prev = last[0]
        
        result = []
        count = 0
        
        for char in last :
            if char == prev:
                count +=1
                continue
            
            result.append(str(count))
            result.append(str(prev))
            
            count = 1
            prev = char
        
        result.append(str(count))
        result.append(str(prev))
        
        return "".join(result)
        
        
        
                
                
                
 
