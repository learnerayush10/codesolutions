#User function Template for python3

class Solution:
    def countDistinctSubarray(self,arr, n): 
        #code here.
        d=dict()
        for i in range(n):
            d[arr[i]]=d.get(arr[i],0)+1
        
        a=len(d)
        hm={}
        ws=0
        c=0
        for i in range(n):
            hm[arr[i]]=hm.get(arr[i],0)+1
            while(len(hm)==a and ws<=i):
                c+=n-i
                hm[arr[ws]]-=1
                if(hm[arr[ws]]==0):
                    del hm[arr[ws]]
                ws+=1
        return c

#{ 
#  Driver Code Starts
#Initial Template for Python 3



t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    ob = Solution()
    print(ob.countDistinctSubarray(a,n))




# } Driver Code Ends