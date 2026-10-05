class Solution:
    def trap(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1

        leftMax = 0
        rightMax = 0

        water = 0

        while i < j:
            if height[i] < height[j]:
                leftMax = max(leftMax, height[i])
                water += leftMax - height[i]
                i += 1

            else:
                rightMax = max(rightMax, height[j])
                water += rightMax - height[j]
                j -= 1
        return water