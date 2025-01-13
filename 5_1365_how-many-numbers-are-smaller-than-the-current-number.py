class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        nsort = sorted(nums)
        d = {}
        ret = []
        for indx, value in enumerate(nsort):
            if value not in d:
                d[value] = indx
            
        for i in nums:
            ret.append(d[i])
        
        return ret