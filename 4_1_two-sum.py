class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for indx, value in enumerate(nums):
            if target-value in hmap:
                return [indx, hmap[target-value]]
            hmap[value] = indx