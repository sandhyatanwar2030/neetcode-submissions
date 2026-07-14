class Solution:
    def isPalindrome(self, s: str) -> bool:
        y=s.lower()
        z=[]
        for ch in y:
            if ch.isalnum():
                z.append(ch)
        return z==z[::-1]
        