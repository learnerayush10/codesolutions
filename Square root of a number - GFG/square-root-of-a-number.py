#User function Template for python3


#Complete this function
class Solution:
    def floorSqrt(self, x):
        if x==1:
            return 1
        i=1
        while i*i<=x:
            i=i+1
        return i-1
    #Your code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math



def main():
        T=int(input())
        while(T>0):
            
            x=int(input())
            
            print(Solution().floorSqrt(x))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends