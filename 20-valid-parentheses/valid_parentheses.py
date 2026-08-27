class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {"(": ")", "{": "}", "[": "]"}
        closing = set(pairs.values())
        stack = []
        for ch in s:
            if ch in pairs:  # opening
                stack.append(ch)
            elif ch in closing:  # closing
                if not stack or pairs[stack.pop()] != ch:
                    return False
        return not stack
