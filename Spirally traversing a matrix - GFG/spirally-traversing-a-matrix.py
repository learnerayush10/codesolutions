#User function Template for python3

class Solution:
    
    #Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self,m, r, c): 
        # code here 
        count=0
        ans=[]
        top=0
        bottom=r-1
        left=0
        right=c-1
        n=r*c
        while(count<n):
            for i in range(left,right+1):
                if(count<n):
                    count=count+1
                    ans.append(m[top][i])
            top+=1
            for i in range(top,bottom+1):
                if(count<n):
                    count+=1
                    ans.append(m[i][right])
            right-=1
            for i in range(right,left-1,-1):
                if(count<n):
                    count+=1
                    ans.append(m[bottom][i])
            bottom-=1
            for i in range(bottom,top-1,-1):
                if(count<n):
                    count+=1
                    ans.append(m[i][left])
            left+=1
        return ans

        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        r,c = map(int, input().strip().split())
        values = list(map(int, input().strip().split()))
        k = 0
        matrix =[]
        for i in range(r):
            row=[]
            for j in range(c):
                row.append(values[k])
                k+=1
            matrix.append(row)
        obj = Solution()
        ans = obj.spirallyTraverse(matrix,r,c)
        for i in ans:
            print(i,end=" ")
        print()

# } Driver Code Ends