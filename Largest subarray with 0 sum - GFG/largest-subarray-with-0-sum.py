#Your task is to complete this function
#Your should return the required output
class Solution:
    def maxLen(self, n, arr):
        #Code here
        temp =[0]
        for a in arr:
            temp.append(temp[-1]+a)
        mp ={}
        for i, t in enumerate(temp):
            if t in mp:
                mp[t][1] =i
            else:
                mp[t] =[i, 0]
        #print(temp, mp)
        return max([mp[tp][1] - mp[tp][0] for tp in mp])
            

#{ 
#  Driver Code Starts
if __name__=='__main__':
    t= int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxLen(n ,arr))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends