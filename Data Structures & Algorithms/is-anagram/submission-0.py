class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #from collections import Counter 
        #return Counter(s) == Counter(t)
        # Or manually
        if len(s) != len(t):
            return False
        def to_dict(s:str):
            count= {}
            for alpha in s:
                count[alpha] = count.get(alpha,0)+1
            return count
        count_s = to_dict(s)
        count_t = to_dict(t)
        return count_s == count_t         
        
        