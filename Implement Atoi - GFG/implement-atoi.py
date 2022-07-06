#User function template for Python

class Solution:
    # your task is to complete this function
    # function should return an integer
    def atoi(self,string):
        # Code here
        mult = 1
        value = 0
        begin = 0
        zero = ord("0")
        nine = ord("9")
        
        if string[0] == "-":
            mult = -1
            begin = 1
        for i in range(begin, len(string)):
            num = ord(string[i])
            if zero <= num <= nine:
                value = (10 * value) + (num - zero)
            else:
                return -1
        return value * mult

#{ 
#  Driver Code Starts
#Initial template for Python

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        string = input().strip();
        ob=Solution()
        print(ob.atoi(string))
# } Driver Code Ends