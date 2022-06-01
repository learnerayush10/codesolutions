class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        PrevMap = {} # val : index
        
        for index, value in enumerate(nums):
            diff = target - value
            
            if diff in PrevMap:
                return [PrevMap[diff], index]
            
            PrevMap[value] = index
        return