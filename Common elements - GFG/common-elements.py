#User function Template for python3

class Solution:
    def commonElements (self,a, b, c, n1, n2, n3):
        # your code here
        a=set(a)
        b=set(b)
        c=set(c)
        dic={}
        arr=[]
        for i in a:
          if(i not in dic):
            dic[i]=1
          else:
            dic[i]+=1
        
        for i in b:
          if(i not in dic):
            dic[i]=1
          else:
            dic[i]+=1
        
        for i in c:
          if(i not in dic):
            dic[i]=1
          else:
            dic[i]+=1
          
        for i in dic:
          if(dic[i]>2):
            arr.append(i)
        
        return(sorted(arr))
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3


t = int (input ())
for tc in range (t):
    n1, n2, n3 = list(map(int,input().split()))
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    C = list(map(int,input().split()))
    
    ob = Solution()
    
    res = ob.commonElements (A, B, C, n1, n2, n3)
    
    if len (res) == 0:
        print (-1)
    else:
        for i in range (len (res)):
            print (res[i], end=" ")
        print ()

# } Driver Code Ends