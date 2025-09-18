class Solution:
    def mySqrt(self, n: int) -> int:
        
        low = 0
        high = n//2 + 1
        
        if n == 1:
            return 1
        
        if n < 1:
            return 0

        while True:

            mid = (low+high)//2

            if (mid*mid < n) and ((mid+1)*(mid+1) > n):
                return mid
                break

            if mid*mid == n:
                return mid
                break

            if mid*mid > n:
                high = mid
            else:
                low = mid
