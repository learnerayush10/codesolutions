#User function Template for python3
class Solution:

	# Function to find maximum
	# product subarray
	def maxProduct(self,arr, n):
		# code here
		p = 1
		maxp = -999999
		for i in arr:
		    p = p*i
		    if p==0:
		        p=1
		    maxp = max(maxp, p)
	    p=1
	    for i in range(n-1, -1, -1):
	        p=p*arr[i]
	        if p==0:
	            p=1
	        maxp = max(maxp, p)
	    return maxp

#{ 
#  Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxProduct(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends