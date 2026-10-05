class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = {}
        s2_count = {}
        for ch in s1:
            s1_count[ch] = s1_count.get(ch, 0) + 1

        i = 0
        have = 0
        target = len(s1_count)

        for j in range(len(s2)):
            s2_count[s2[j]] = s2_count.get(s2[j], 0) + 1

            if s2[j] in s1_count and s1_count[s2[j]] == s2_count[s2[j]]:
                have += 1
            
            # window badi ho gayi to left hatao            
            if j - i + 1 > len(s1):
                if s2[i] in s1_count and s1_count[s2[i]] == s2_count[s2[i]]:
                    have -= 1
                s2_count[s2[i]] -= 1 
                i += 1
                
            if have == target:
                return True
        
        return False

        


        