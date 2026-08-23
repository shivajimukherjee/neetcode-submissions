from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Constraint check: If lengths differ, they cannot be anagrams
        if len(s) != len(t):
            return False
            
        return Counter(s) == Counter(t)