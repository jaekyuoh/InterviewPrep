
class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        complement = {}
        for idx in range(len(nums)):
            complement[nums[idx]] = idx
        for i in range(len(nums)):
            temp = target - nums[i]
            if temp in complement and i != complement[temp]:
                return [i, complement[temp]]
            # complement[nums[i]] = i
        return []


if __name__ == '__main__':
    nums = [0, 1, 3, 5, 6]
    target = 9
    solution = Solution()
    print(solution.twoSum(nums=nums, target=target))