class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def two_words(prev, current):
            prefix = ""
            while current and prev:
                if prev[0] == current[0]:
                    prefix += prev[0]
                else:
                    return prefix
                current = current[1:]
                prev = prev[1:]
            return prefix

        prefix = strs[0]
        for i, word in enumerate(strs, start=1):
            pref = two_words(prefix, word)
            prefix = pref
        return prefix
