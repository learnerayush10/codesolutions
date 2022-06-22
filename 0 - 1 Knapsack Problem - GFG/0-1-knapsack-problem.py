#User function Template for python3

class Solution:
    def Knapsack_recursion(self,i,weight,value,n,size,dp):
        if i == n:
            if size == 0:
                return 0
            return 0
        if dp[i][size] != -1: return dp[i][size]
        pick = 0
        if size >= weight[i]:
            pick = self.Knapsack_recursion(i+1,weight,value,n,size-weight[i],dp) + value[i]
        notpick = self.Knapsack_recursion(i + 1, weight, value, n, size,dp)
        dp[i][size] =  max(pick,notpick)
        return dp[i][size]
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
        dp = [[-1]*(W+1) for _ in range(n+1)]
        for k in range(W+1):
            dp[n][k] = 0
        
        for i in reversed(range(n)):
            for j in reversed(range(W+1)):
                pick = 0
                if j >= wt[i]:
                    pick = dp[i+1][j-wt[i]] + val[i]
                notpick = dp[i+1][j]
                dp[i][j] = max(pick,notpick)
        return dp[0][W]

       
        # code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        W = int(input())
        val = list(map(int,input().strip().split()))
        wt = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.knapSack(W,wt,val,n))
# } Driver Code Ends