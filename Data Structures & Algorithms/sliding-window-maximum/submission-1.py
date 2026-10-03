class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []                  
        dq = collections.deque() # store index
        i = 0

        while i < len(nums):
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            dq.append(i)

            if i - k >= dq[0]:
                dq.popleft()
            
            if i >= k - 1:
                output.append(nums[dq[0]])
            i += 1
        return output
            