class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        max_freq = 0
        i = 0
        best = 0
        for j in range(len(s)):
            freq[s[j]] = freq.get(s[j], 0) + 1
            max_freq = max(max_freq, freq[s[j]])
            if (j - i + 1) - max_freq > k:
                freq[s[i]] -= 1
                i += 1
            best = max(best, j - i + 1)
        return best


