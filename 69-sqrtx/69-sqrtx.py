class Solution:
    def mySqrt(self, x: int) -> int:
        high = x
        low = 0
        
        while high >= low:
            mid = (high + low) // 2
            midsq = mid * mid
            if x > midsq:
                low = mid + 1
            elif x < midsq:
                high = mid - 1
            else:
                return mid

        if mid*mid < x:
            return mid
        else:
            return mid - 1