from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        for n in nums:
            hashmap[n] += 1

        lookup_list = [[] for i in range(len(nums))]
        for key in hashmap:
            val = hashmap[key]
            lookup_list[val-1].append(key)
        
        res = []
        for i in reversed(lookup_list):
            if i is not []:
                for nums in i:
                    res.append(nums)
                    if len(res) == k:
                        return res
