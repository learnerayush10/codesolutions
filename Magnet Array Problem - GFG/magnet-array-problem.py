#User function Template for python3

class Solution:
    def nullPoints(self, n, a, getAnswer):
        z = 0
        
        for i in range(n-1):
            start = a[i]
            end = a[i + 1]
            while True:
                mid = (start + end)/2
                eq = self.equilibrium(a, mid)
                #print(start,end, mid,eq)
                if eq > 0:
                    start = mid
                elif eq < 0:
                    end = mid
                else:
                    #print(mid)
                    getAnswer[i] = (mid)
                    break

    def equilibrium(self, a, mid):
        ans = 0
        for i in range(len(a)):
            if mid - a[i] != 0:
                ans = ans + 1/(mid  - a[i])
        
        return round(ans,5)




#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        getAnswer = [0]*n
        ob=Solution()
        ob.nullPoints(n, a, getAnswer)
        
        for i in range(0,n-1):
            print("{:.2f}".format(getAnswer[i]), end=" ")
        print()

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends