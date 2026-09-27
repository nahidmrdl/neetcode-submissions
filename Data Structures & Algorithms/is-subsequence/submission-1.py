class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        p = 0
        tp = 0
        while p < len(s) and tp < len(t):
            if s[p] != t[tp]:
                tp += 1
            elif s[p] == t[tp]:
                p += 1
                tp += 1
                
        return p == len(s)
