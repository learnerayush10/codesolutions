class Solution:
    def duplicates(self, arr, n): 
    	# code here
    	i=0
        j=len(arr)-1
        arr2=set()
        s=set()
        s.add(arr[0])
        for i in range(1,n):
            temp_len=len(s)
            s.add(arr[i])
            if(temp_len==len(s)):
                arr2.add(arr[i])
        if(len(arr2)==0):
            arr2.add(-1)
        return sorted(arr2)
        return arr2
    	    

#{ 
#  Driver Code Starts
if(__name__=='__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = Solution().duplicates(arr, n)
        for i in res:
            print(i,end=" ")
        print()



# } Driver Code Ends