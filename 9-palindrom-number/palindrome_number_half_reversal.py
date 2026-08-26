def isPalindrome(x: int) -> bool:
    if x == 0:
        return True
    if x < 0 or (x % 10 == 0 and x != 0):
        return False

    reversed_half = 0
    while x > reversed_half:
        remainder = x % 10
        x = x // 10
        reversed_half = reversed_half * 10 + remainder

    return x == reversed_half or reversed_half // 10 == x
