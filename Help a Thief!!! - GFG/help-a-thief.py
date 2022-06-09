#User function Template for python3

class Solution:
    def maxCoins(self, A, B, T, N):
        # code here
        dp=[]
        for i in range(N):
            dp.append([A[i],B[i]])
        dp.sort(key=lambda x:x[1])
        
        # print(dp)
        total=0
        i=N-1
        while i>-1 and T>0:
            if dp[i][0]<=T:
                total+=(dp[i][1]*dp[i][0])
                T-=dp[i][0]
            else:
                total+=T*dp[i][1]
                T=0
            i-=1    
        return total        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        T,N=map(int,input().split())
        A=list(map(int,input().split()))
        B=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.maxCoins(A,B,T,N))
# } Driver Code Ends