
class Solution:
    def minSum(self, arr, n):
        # Your code goes here
        arr.sort()
        a,b=0,0
        ok = True
        for val in arr:
            if ok:
                a = (a*10) + val
            else:
                b = (b*10) + val
            ok = 1^ ok
        return a+b
    

#{ 
#  Driver Code Starts

import heapq as hq

if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        n = int(input())
        arr = [int(x) for x in input().split()]
        ob=Solution()
        print(ob.minSum(arr,n))

# } Driver Code Ends