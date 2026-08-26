def romanToInt(s: str) -> int:
    r = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    for i in range(len(s) - 1):
        current = r[s[i]]
        next_ = r[s[i + 1]]

        if current < next_:
            total -= current
        else:
            total += current

    return total + r[s[-1]]
