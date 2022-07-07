#User function Template for python3

class Solution:
    
    #Function to merge the arrays.
    def merge(self,arr1,arr2,n,m):
        A = [i for i in arr1]
        for ele in arr2:
            A.append(ele)
        A.sort()
        ind=0
        for i in range(n):
            arr1[i] = A[ind]
            ind += 1
        for j in range(m):
            arr2[j] = A[ind]
            ind += 1
        #code here
    


#{ 
#  Driver Code Starts
#Initial template for Python

if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        n,m = map(int, input().strip().split())
        arr1 = list(map(int, input().strip().split()))
        arr2 = list(map(int, input().strip().split()))
        ob=Solution()
        ob.merge(arr1, arr2, n, m)
        print(*arr1,end=" ")
        print(*arr2)
# } Driver Code Ends