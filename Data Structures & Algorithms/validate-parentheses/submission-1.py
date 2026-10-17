class Solution:
    def isValid(self, s: str) -> bool:

        pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
        }

        stack = []

        for c in s:
            if c in "([{":
                stack.append(c)

            else: 
                if not stack or pairs[c] != stack[-1]:
                    return False
                
                stack.pop()
        

        return not stack