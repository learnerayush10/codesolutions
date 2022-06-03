#User function Template for python3

class Solution:
    def isPossible(self, s, n, x, a):
        # code here
        d=[s]
        for i in a:
            c=s
            s+=i
            d.append(s)
            s+=c
        # print(d)
        for i in range(n,-1,-1):
            if x>=d[i]: x-=d[i]
            if x==0: return True
        return False

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S, N, X = [int(y) for y in input().split()]
        A = input().split()
        for i in range(N):
            A[i] = int(A[i])
        
        ob = Solution()
        if ob.isPossible(S, N, X, A) == 1:
            print("yes")
        else:
            print("no")
# } Driver Code Ends