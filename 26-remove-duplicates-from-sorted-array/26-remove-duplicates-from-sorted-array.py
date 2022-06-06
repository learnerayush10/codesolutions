class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = len(nums)
        pop_offset = 0
        for i in range(1,l):
            i = i-pop_offset
            if nums[i]==nums[i-1]:
                nums.pop(i)
                pop_offset+=1