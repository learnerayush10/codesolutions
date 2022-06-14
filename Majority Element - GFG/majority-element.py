#User function template for Python 3

class Solution:
    def majorityElement(self, A, N):
        #Your code here
        mapx = dict()
        for i in range(N):
            if A[i] not in mapx:
                mapx[A[i]] =1
            else:
                mapx[A[i]] +=1
            if mapx[A[i]] > N//2:
                return A[i]
        return -1
                

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

from sys import stdin


def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=[int(x) for x in input().strip().split()]
            
            
            obj = Solution()
            print(obj.majorityElement(A,N))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends