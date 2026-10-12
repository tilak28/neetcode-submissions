class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        A, B = nums1, nums2
        if len(A) > len(B):          # A hamesha chhota
            A, B = B, A

        m, n = len(A), len(B)
        half = (m + n + 1) // 2      # left side me kitne elements chahiye

        l, r = 0, m                  # i ki range: 0 se m

        while l <= r:
            i = (l + r) // 2         # A se left me kitne
            j = half - i             # B se left me kitne

            Aleft  = A[i - 1] if i > 0 else float('-inf')
            Aright = A[i]     if i < m else float('inf')
            Bleft  = B[j - 1] if j > 0 else float('-inf')
            Bright = B[j]     if j < n else float('inf')

            if Aleft <= Bright and Bleft <= Aright:     # valid cut
                #ODD
                if (m + n) % 2:
                    return max(Aleft, Bleft)
                #EVEN
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1            # A se zyada le liye, kam karo
            else:
                l = i + 1            # A se kam le liye, badhao