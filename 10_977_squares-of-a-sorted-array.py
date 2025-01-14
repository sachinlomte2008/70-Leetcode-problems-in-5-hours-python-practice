class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if not nums:
            return nums
        
        if nums[0] >= 0:
            return [num**2 for num in nums]
        
        part = -1
        for idx, num in enumerate(nums):
            if num >=0:
                part = idx
                break
        
        if part == -1:
            return [num**2 for num in reversed(nums)]
            
        list1, list2 = nums[part:], [-1*num for num in reversed(nums[:part])]

        def mergeSquared(list1, list2):
            len1 = len(list1)
            len2 = len(list2)
            i, j = 0, 0
            ans = []

            while i < len1 and j < len2:
                if list1[i] < list2[j]:
                    ans.append(list1[i])
                    i+=1
                else:
                    ans.append(list2[j])
                    j+=1
            
            if i < len1:
                ans.extend(list1[i:])
            if j < len2:
                ans.extend(list2[j:])
            
            ans = [n**2 for n in ans]
            return ans

        return mergeSquared(list1, list2)
    

'''
# better solution
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        final = []
        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                final.append(nums[left]**2)
                left+=1

            else:
                final.append(nums[right]**2)
                right-=1

        return final[::-1]
'''