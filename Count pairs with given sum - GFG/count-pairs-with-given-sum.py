#User function Template for python3

class Solution:
    def getPairsCount(self, arr, n, k):
        # code here
        sumsofar=0
        count=0
        history=dict()
        for i in arr:
            if k-i in history:
                count+=history[k-i]
            history[i]=history.get(i,0)+1
        return count

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getPairsCount(arr, n, k)
        print(ans)
        tc -= 1

# } Driver Code Ends