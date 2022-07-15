#User function Template for python3


class Solution:
    
    #Function to find the maximum number of cuts.
    def maximizeTheCuts(self,n,x,y,z):
        #code here
        dp=[-1]*(n+1)
        dp[0]=0
        for i in range(1, n+1):
            if x<=i and dp[i-x]!=-1:
                dp[i]=max(dp[i],1+dp[i-x])
            if y<=i and dp[i-y]!=-1:
                dp[i]=max(dp[i],1+dp[i-y])
            if z<=i and dp[i-z]!=-1:
                dp[i]=max(dp[i],1+dp[i-z])
        return 0 if dp[n]== -1 else dp[n]

#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__':
    t=int(input())
    for tcs in range(t):
        n=int(input())
        x,y,z=[int(x) for x in input().split()]
        
        print(Solution().maximizeTheCuts(n,x,y,z))
# } Driver Code Ends