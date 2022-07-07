#User function Template for python3

from math import inf
class Solution:
    def get_matrices(self, path, i, j):
        if j == i + 1:
            return chr(i + ord('A'))
        else:
            return '(' + self.get_matrices(path, i, path[i][j]) +\
                    self.get_matrices(path, path[i][j], j) + ')'
        
        
    def matrixChainOrder(self, p, n):
        dp = [[0 for j in range(n)] for i in range(n)]
        path = [[None for j in range(n)] for i in range(n)]
        
        for c in range(2, n):
            for i in range(n - c):
                j = i + c
                dp[i][j] = inf
                for k in range(i+1, j):
                    cur = dp[i][k] + dp[k][j] + p[i]*p[k]*p[j]
                    if dp[i][j] > cur:
                        dp[i][j] = cur
                        path[i][j] = k
     
        return self.get_matrices(path, 0, n-1)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        p = input().split()
        for i in range(n):
            p[i] = int(p[i])
        
        ob = Solution()
        print(ob.matrixChainOrder(p, n))
# } Driver Code Ends