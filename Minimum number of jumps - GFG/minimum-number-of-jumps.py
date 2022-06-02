#User function Template for python3
class Solution:
	def minJumps(self, arr, n):
	    #code here
	    far = 0; jumps = 0; curr = 0
        
        for i in range(n-1):
            
            far = max(far, i+arr[i])
            
            if i == curr:
                jumps += 1
                curr = far
                
       
        if curr < n-1:
            return -1
            
        return jumps
#{ 
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		Arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minJumps(Arr,n)
		print(ans)
# } Driver Code Ends