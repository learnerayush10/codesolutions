#User function template for Python

class Solution:	
	def buzzTime(self, N, M, L, H, A):
		# code here
		l = 0
		r = 0
		x = max(M, L)
		for i in range(N):
		    if((x- H[i])%A[i] == 0):
		        r = max(r, (x-int(H[i])/A[i]))
		    else:
		        r = max(r, (x - int(H[i])/A[i]) + 1)
		while(l <=r):
		    mid = int((l+r)/2)
		    sum = 0
		    for i in range(N):
		        if((H[i] + A[i]*mid) >= L):
                    sum += (H[i] + A[i]*mid)
            if(sum >= M):
                r = mid-1
            else:
                l = mid+1
        return l
#{ 
#  Driver Code Starts
#Initial template for Python

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, M, L = [int(x) for x in input().split()]
        H = [0 for x in range(N)]
        A = [0 for x in range(N)]
        for i in range(N):
            H[i], A[i] = [int(y) for y in input().split()]
        ob = Solution()
        print(ob.buzzTime(N, M, L, H, A))

# } Driver Code Ends