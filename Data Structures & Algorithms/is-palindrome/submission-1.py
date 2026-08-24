class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""
        for a in s:
            if a.isalnum():
                cleaned += a.lower()
        for i in range(len(cleaned)//2):
            if cleaned[i] != cleaned[len(cleaned)-i-1]:
                return False
        return True
        