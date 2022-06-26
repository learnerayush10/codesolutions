#User function Template for python3

class Solution:
    
    #Function to find if there is a celebrity in the party or not.
    def celebrity(self, M, n):
        count=0
        storing_j=-1
        for i in range(0,n):
            for j in range(0,n):
                if M[i][j]==0:
                    count+=1
                if count==n:
                    storing_j=i
                    break
            count=0
        if storing_j==-1:
            return -1
        for i in range(0,n):
            if i==storing_j:
                continue
            else:
                if M[i][storing_j]==0:
                    return -1
        return storing_j


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t) :
        n = int(input())
        a = list(map(int,input().strip().split()))
        k = 0
        m = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(a[k])
                k+=1
            m.append(row)
        ob = Solution()
        print(ob.celebrity(m,n))
# } Driver Code Ends