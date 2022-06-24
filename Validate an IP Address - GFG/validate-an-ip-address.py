#User function Template for python3

def isValid(s):
    x=["a","b","c","e","o"]
    a=[]
    for i in s.split("."):
        if s.count(".")==3 and i not in x and i!= "00" and i!= "000" and i!= "0000" and i!="" and len(str(int(i)))==len(i) :
            j=int(i)
            if j>=0 and j<=255:
                a.append(1)
            else:
                a.append(0)
    if a.count(1)==4:
        return 1
    else:
        return 0


#{ 
#  Driver Code Starts
#Initial Template for Python 3

    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        if(isValid(s)):
            print(1)
        else:
            print(0)
    

# } Driver Code Ends