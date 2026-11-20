
class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        add = 0
        tot = (n * (n + 1)) // 2

        for num in nums:
            add += num

        if tot - add != 0:
            return tot - add
        else:
            return 0
