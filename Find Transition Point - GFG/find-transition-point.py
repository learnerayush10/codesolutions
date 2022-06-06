def transitionPoint(arr, n):
    #Code here
    start= 0
    end = n-1
    mid = 0
    while(start<=end):
        mid=(start+end)//2
        if(arr[mid]!=arr[mid-1]):
            return mid
        elif(arr[mid]==arr[mid-1] and arr[mid]==arr[0]):
            start=mid+1
        elif(arr[mid]==arr[mid-1] and arr[mid]!=arr[0]):
            end=mid-1
    if set(arr)=={1}:
        return 0
    else:
        return -1
#{ 
#  Driver Code Starts
#driver code
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(transitionPoint(arr, n))

# } Driver Code Ends