class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        count = {}

        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        for ch in t:
            if ch not in count:
                return False

            count[ch] -= 1

            if count[ch] < 0:
                return False

        return True

        
        # s = list(s)
        # t = list(t)

        # s.sort()
        # t.sort()

        # return s == t
        # if len(s)!= len(t):
        #     return False
        # else:
        #     char1 = list(s)
        #     char2 = list(t)
        #     char1.sort()
        #     char2.sort()
        #     return char1==char2 
 
        
        