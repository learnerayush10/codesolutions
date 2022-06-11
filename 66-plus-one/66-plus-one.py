class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        right_pointer = len(digits) - 1
        increment = 1
        
        while right_pointer >= 0 and increment > 0:
            if digits[right_pointer] == 9:
                digits[right_pointer] = 0
                right_pointer -= 1
            elif digits[right_pointer] != 9:
                digits[right_pointer] += 1
                increment += 1
                return digits
        return [1] + digits