#User function Template for python3

# design the class in the most optimal way

from collections import OrderedDict
class LRUCache:
      
    #Constructor for initializing the cache capacity with the given value.  
    def __init__(self,cap):
        #code here
        self.cap=cap
        self.d=OrderedDict()
        
    #Function to return value corresponding to the key.
    def get(self, key):
        #code here
        if key not in self.d:
            return -1
        else:
            self.d.move_to_end(key)
            return self.d[key]
            
        
    #Function for storing key-value pair.   
    def set(self, key, value):
        #code here
        self.d[key]=value
        self.d.move_to_end(key)
        if(len(self.d)>self.cap):
            self.d.popitem(last = False)



#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        cap = int(input())  # capacity of the cache
        qry=int(input())  #number of queries
        a = list(map(str, input().strip().split()))  # parent child info in list
        
        lru=LRUCache(cap)
        
       
        i=0
        q=1
        while q<=qry:
            qtyp=a[i]
            
            if qtyp=='SET':
                lru.set(int(a[i+1]),int(a[i+2]))
                i+=3
            elif qtyp=='GET':
                print(lru.get(int(a[i+1])),end=' ')
                i+=2
            q+=1
        print()
# } Driver Code Ends