#User function Template for python3

class Solution:
    def findNum(self, n : int):
        # Complete this function
        num_found = False
        tot = 0
        num = 5
        fact = 5
        start = 1
        end = 5*n
        while start<=end:
            mid = start+(end-start)//2
            count = 0
            temp = mid
            while mid!=0:
                count += mid//5
                mid=mid//5
            if count >=n:
                end = temp -1
            else:
                start = temp+1
        return start

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        ob = Solution()
        print(ob.findNum(n))
# } Driver Code Ends