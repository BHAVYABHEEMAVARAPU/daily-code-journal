
class Solution:
    def reverse(self, x: int) -> int:
        n = len(str(abs(x)))
        l = abs(x)
        rev = 0

        for i in range(n):
            num = l % 10
            rev = rev * 10 + num
            l = l // 10

        if x < 0:
            rev = -rev

        if rev < -(2**31) or rev > 2**31 - 1:
            return 0

        return rev
