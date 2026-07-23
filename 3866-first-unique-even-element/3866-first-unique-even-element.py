class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        c = {}

        for num in nums:
            if num not in c:
                c[num] = 1
            else:
                c[num] += 1

        for num in nums:
            if c[num] == 1 and num % 2 == 0:
                return num

        return -1