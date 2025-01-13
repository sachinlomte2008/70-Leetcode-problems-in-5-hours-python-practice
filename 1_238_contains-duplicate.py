class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nset = set()
        for i in nums:
            if i in nset:
                return True
            nset.add(i)
        return False