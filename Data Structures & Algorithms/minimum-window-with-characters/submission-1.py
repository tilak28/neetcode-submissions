class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        for ch in t:
            need[ch] = need.get(ch, 0) + 1

        window = {}
        have = 0
        needCount = len(need)

        i = 0
        best_len = float('inf')
        best_start = 0

        for j in range(len(s)):
            if s[j] in need:
                window[s[j]] = window.get(s[j], 0) + 1
                
                if need[s[j]] == window[s[j]]:
                    have += 1
            
            while have == needCount:
                if (j - i + 1) < best_len:
                    best_len = j - i + 1
                    best_start = i
                
                if s[i] in need:
                    window[s[i]] -= 1
                    if window[s[i]] < need[s[i]]:
                        have -= 1
                i += 1
        if best_len == float('inf'):
            return ""
        else:
            return s[best_start: best_start + best_len]


            





            