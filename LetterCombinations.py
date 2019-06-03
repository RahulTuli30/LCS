import itertools
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        lists_to_merge = self.get_lists_to_merge(digits, self.get_digit_dict())
        
        combinations = ["".join(combination) for combination in itertools.product(*lists_to_merge)]
        return combinations
        
        
    def get_lists_to_merge(self, s, digit_dict):        
        result = []
        for digit in s:
            result.append(digit_dict[digit])    
        return result
    
    def get_digit_dict(self):
        digit_dict = {}
        letter = ord('a')
        for i in '23456789':
            digit_dict[i] = [chr(element) for element in range(letter, letter + 3)]
            letter += 3
            
            if i is '7' or i is '9':
                digit_dict[i].append(chr(letter))
                letter += 1
        
        return digit_dict
  
