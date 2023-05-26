class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for idx, n in enumerate(nums):
            diff = target - n
            if diff in hashmap:
                return [idx, hashmap[diff]]
            hashmap[n] = idx
