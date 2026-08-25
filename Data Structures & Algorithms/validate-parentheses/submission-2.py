class Solution:
    def isValid(self, s: str) -> bool:
        corresp = {
            '}': '{',
            ']': '[',
            ')': '('
        }
        # We can implement a last in first out method
        stack = []
        for char in s:
            if char in corresp: # closing brackets
                if not stack or corresp[char] != stack[-1]:
                    return False
                else:
                    stack.pop()
            else:# opening brackets
                stack.append(char)
        return not stack


            
            
        