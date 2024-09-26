class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        m = {}
        for num in nums:
            if m[num] == 1:
                return True
            m[num] = 1
        return False
