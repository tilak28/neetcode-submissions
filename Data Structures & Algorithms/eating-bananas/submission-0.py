class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        i = 1
        j = max(piles)

        res = j

        while i <= j:
            hours = 0
            k = (i + j ) // 2 # k -> mid, speed of eating bananas

            for p in piles:
                hours += math.ceil(p / k)
            
            if hours <= h:
                res = k
                j = k - 1
            else:
                i = k + 1
        return res
