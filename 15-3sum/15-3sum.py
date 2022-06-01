class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        result: List[List[int]] = []
        nums.sort()
        
        for index in range(len(nums)):
            if index != 0 and nums[index-1] == nums[index]:
                continue
            
            left, right = index+1, len(nums)-1
            
            while left < right:
                sm = nums[index] + nums[left] + nums[right]
                if sm > 0:
                    right -= 1
                elif sm < 0:
                    left += 1
                else:
                    result.append([nums[index], nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
                    
        return result