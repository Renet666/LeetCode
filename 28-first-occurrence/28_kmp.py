def strStr(haystack: str, needle: str) -> int:
    n = len(needle)
    length = 0
    lps = [0] * n
    for i in range(1, n):
        while length > 0 and needle[i] != needle[length]:
            length = lps[length - 1]

        if needle[i] == needle[length]:
            length += 1
        lps[i] = length

    i = 0
    j = 0
    while i < len(haystack) and j < n:
        if haystack[i] == needle[j]:
            i += 1
            j += 1
        else:
            if j > 0:
                j = lps[j - 1]
            else:
                i += 1
        if j == n:
            return i - n
    return -1


print(strStr(haystack="leetcode", needle="leeto"))
