#User function Template for python3

class Solution:
    
    #Function to check whether there is a subarray present with 0-sum or not.
    def subArrayExists(self,arr,n):
        ##Your code here
        #Return true or false
        a=[0]*n
        a[0]=arr[0]
        for i in range(1, n):
            a[i] =a[i-1]+arr[i]
        d={}
        flag=0
        for i in range(n):
            if a[i] in d:
                flag = 1
                return True
            elif a[i]==0:
                return True
            else:
                d[a[i]]=1
        if flag==0:
            return False

#{ 
#  Driver Code Starts
#Initial Template for Python 3



def main():
    T=int(input())
    while(T>0):
        
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        if(Solution().subArrayExists(arr,n)):
            print("Yes")
        else:
            print("No")
        
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends