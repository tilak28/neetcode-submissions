class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        i = max(weights)
        j = sum(weights)
        res = j


        while i <= j:
            m = (i + j) // 2
            min_days = 1
            load = 0

            for p in weights:
                if p + load > m:
                    min_days += 1
                    load = 0
                load += p
            
            if min_days <= days:
                res = m
                j = m - 1
            else:
                i = m + 1
        return res 
                 
                    