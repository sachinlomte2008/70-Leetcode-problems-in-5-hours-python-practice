class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        nums = sorted(nums)
        i = 0

        while i < n:
            target = -nums[i]
            front = i+1
            back = n-1
            while(front < back):
                if (nums[front] + nums[back]) < target:
                    front += 1
                elif (nums[front] + nums[back]) > target:
                    back -= 1
                else:
                    temp = []
                    temp.append(nums[i])
                    temp.append(nums[front])
                    temp.append(nums[back])
                    ans.append(temp)
                    while(front<back and nums[front]==temp[1]):
                        front+=1
                    while(front<back and nums[back]==temp[2]):
                        back-=1
            
            while(i+1<n and nums[i+1]==nums[i]):
                i+=1

            i+=1

        return ans