class Solution:
    def isValid(self, s: str) -> bool:
        corresp = {
            '}': '{',
            ']': '[',
            ')': '('
        }
        # We can implement a last in first out method
        list = []
        for char in s:
            if char in corresp.values():
                list.append(char)
            else:
                corresp_char = corresp.get(char)
                if not list or corresp_char != list[-1]:
                    return False
                list.pop()
        return not list


            
            
        