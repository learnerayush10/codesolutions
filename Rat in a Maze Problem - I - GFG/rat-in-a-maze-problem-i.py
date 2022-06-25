#User function Template for python3

class Solution:
    def healper(self,n,i,j,arr,ans,cur,visted):
        if (i<0 or j<0 or i==n or j==n or arr[i][j]==0 or visted[i][j]==True):
            return 
        if (i==n-1 and j==n-1 and arr[i][j]==1):
            temp="";
            for i in cur:
                temp+=i;
            ans.append(temp);
            return
        
        visted[i][j]=True;
        cur.append('L')
        self.healper(n,i,j-1,arr,ans,cur,visted)
        cur.pop();
        cur.append('D')
        self.healper(n,i+1,j,arr,ans,cur,visted)
        cur.pop();
        cur.append('U')
        self.healper(n,i-1,j,arr,ans,cur,visted)
        cur.pop();
        cur.append('R')
        self.healper(n,i,j+1,arr,ans,cur,visted)
        cur.pop();
        visted[i][j]=False;
    def findPath(self, arr, n):
        visted=[[False]*n for i in range(n)]
        # visted[0][0]=True
        ans=[]
        cur=[]
        self.healper(n,0,0,arr,ans,cur,visted);
        return ans;

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        
        matrix = [[0 for i in range(n[0])]for j in range(n[0])]
        k=0
        for i in range(n[0]):
            for j in range(n[0]):
                matrix[i][j] = arr[k]
                k+=1
        ob = Solution()
        result = ob.findPath(matrix, n[0])
        result.sort()
        if len(result) == 0 :
            print(-1)
        else:
            for x in result:
                print(x,end = " ")
            print()
# } Driver Code Ends