#User function Template for python3

class Solution:
    
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V, adj):
        # code here
       visit=[]
       queue=[]
       result=[]
       
       visit.append(0)
       queue.append(0)
       
       while (queue):
           m=queue.pop(0)
           result.append(m)
           for i in adj[m]:
               if i not in visit:
                   visit.append(i)
                   queue.append(i)
                   
       return result

#{ 
#  Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
		ob = Solution()
		ans = ob.bfsOfGraph(V, adj)
		for i in range(len(ans)):
		    print(ans[i], end = " ")
		print()
        

# } Driver Code Ends