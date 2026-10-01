class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        for ch in t:
            need[ch] = need.get(ch,0) +1 

        window = {}
        i = 0
        have = 0
        best_start = 0
        best_length = float('inf')

        for j in range(len(s)):
            if s[j] in need:
                window[s[j]] = window.get(s[j], 0) + 1

                if need[s[j]] == window[s[j]]:
                    have += 1
            while have == len(need):
                if j - i + 1 < best_length:
                    best_length = j - i + 1
                    best_start = i
                
                if s[i] in need:
                    window[s[i]] -= 1
                    if window[s[i]] < need[s[i]]:
                        have -= 1
                i += 1

        if best_length == float('inf'):
            return ""
        else:
            return s[best_start: best_start + best_length]


        