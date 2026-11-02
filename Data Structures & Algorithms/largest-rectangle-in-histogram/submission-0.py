class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        st = []
        MaxArea = 0

        for i in range(n + 1):
            h = heights[i] if i < n else 0 
            
            while st and h < heights[st[-1]]:
                height = heights[st[-1]] 
                st.pop()
                
                left = st[-1] if st else -1

                width = i - left - 1
                area = height * width
                MaxArea = max(area, MaxArea)
            st.append(i)

        return MaxArea 
