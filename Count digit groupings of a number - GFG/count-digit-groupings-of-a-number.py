#User function Template for python3

class Solution:
    def TotalCount(self, s):
        # Code here
        total=0
        for ch in s:
            total+=int(ch)
        n=len(s)
        dp=[[-1]*(n+1) for _ in range(total+1)]
        
        def dfs(prev,pos):
            if pos==n:
                return 1
            if dp[prev][pos]!=-1:
                return dp[prev][pos]
            
            res=0
            cur=0
            for i in range(pos,n):
                cur+=int(s[i])
                if cur>=prev:
                    res+=dfs(cur,i+1)
            
            dp[prev][pos]=res
            return res
        
        return dfs(0,0)


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		ob = Solution()
		ans = ob.TotalCount(s)
		print(ans)
# } Driver Code Ends