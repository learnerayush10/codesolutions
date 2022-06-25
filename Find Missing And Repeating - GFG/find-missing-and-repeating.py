#User function Template for python3

class Solution:
    def findTwoElement( self,arr, n): 
        d={}
        l=[]
        for i in arr:
            d[i]=d.get(i,0)+1
        for ind,val in enumerate(d):
            if d[val]>=2:
                l.append(val)
        for ind,val in enumerate(d):
            c=ind+1
            if(ind+1) not in d:
                l.append(ind+1)
                return l
        l.append(c+1)
        return l

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int, input().strip().split()))
        ob = Solution()
        ans=ob.findTwoElement(arr, n)
        print(str(ans[0])+" "+str(ans[1]))
        tc=tc-1
# } Driver Code Ends