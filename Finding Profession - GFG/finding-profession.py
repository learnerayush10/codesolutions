#User function Template for python3

class Solution:
    def profession(self, level, pos):
        # code here
       if(pos==1):
           return 'e'
       par=self.profession(level-1,(pos+1)//2)
       if pos%2 !=0:
           return par
       if par=='e':
           return 'd'
           
       else:
           return 'e'


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        level, pos = [int(x) for x in input().split()]
        
        ob = Solution()
        if(ob.profession(level, pos) == 'd'):
            print("Doctor")
        else:
            print("Engineer")
# } Driver Code Ends