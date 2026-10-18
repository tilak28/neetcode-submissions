class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}

        for i in range(len(s)):
            if s[i] in pairs:
                if stack and stack[-1] == pairs:
                    stack.pop()

                else:
                    return False
            else:
                stacka.ppend(s[i])
        
        return True if not stack else False

