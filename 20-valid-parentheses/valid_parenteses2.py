class Solution:
    def isValid(self, s: str) -> bool:
        d = {"()", "{}", "[]"}
        stack = []  # only opening brackets
        opening_brackets = ("(", "{", "[")
        closing_brackets = (")", "}", "]")

        for bracket in s:
            if bracket in opening_brackets:
                stack.append(bracket)
            if bracket in closing_brackets:
                if stack:
                    popped = stack.pop()
                    brackets = popped + bracket
                    if brackets in d:
                        continue
                    else:
                        return False
                else:
                    return False
        return not stack
