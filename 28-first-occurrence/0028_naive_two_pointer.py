class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        haystack_len = len(haystack)
        needle_len = len(needle)
        
        i = 0  # position in haystack
        j = 0  # position in needle
        
        while j < needle_len and i < haystack_len:
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                # Backtrack: move to the next starting character
                i = i - j + 1
                j = 0
                
        return i - j if j == needle_len else -1