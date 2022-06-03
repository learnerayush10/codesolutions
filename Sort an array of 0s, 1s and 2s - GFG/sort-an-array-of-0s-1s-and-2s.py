#User function Template for python3

class Solution:
    def fill_array(self, arr, itr, cnt, fill):
        for i in range(itr, cnt):
            arr[i] = fill
            
    def sort012(self,arr,n):
        # code here
        num_1s = 0
        num_2s = 0
        num_0s = 0
        
        for a in arr:
            if a == 0:
                num_0s += 1
            elif a == 1:
                num_1s += 1
            else:
                num_2s += 1
        
        self.fill_array(arr, 0, num_0s, 0)
        self.fill_array(arr, num_0s, num_0s + num_1s, 1)
        self.fill_array(arr, num_0s + num_1s, num_0s+num_1s+num_2s, 2)



#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends