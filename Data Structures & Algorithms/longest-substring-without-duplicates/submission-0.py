class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sett = set()
        i = 0
        longest = 0
        
        for j in range (len(s)):
            while s[j] in sett:
                sett.remove(s[i])
                i += 1
            
            w = (j - i) + 1
            
            longest = max(longest, w)
            sett.add(s[j])
        
        return longest