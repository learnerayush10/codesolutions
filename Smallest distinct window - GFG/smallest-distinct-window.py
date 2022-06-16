#User function Template for python3
from collections import defaultdict as dd
class Solution:
    def findSubString(self, str):
        # Your code goes here
        letters = set()
        for ch in str:
            letters.add(ch)
        n = len(letters)
        shortest = len(str)
        letters = dd(int)
        l = 0
        r = 0
        while r < len(str):
            letters[str[r]] +=1
            r += 1
            if len(letters) == n:
                while len(letters) == n:
                    letters[str[l]] -= 1
                    if letters[str[l]] == 0:
                        del letters[str[l]]
                    l += 1
                shortest = min(shortest, r-l+1)
        return shortest
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
    	str = input()
    	ob=Solution()
    	print(ob.findSubString(str))
    	
    	T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends