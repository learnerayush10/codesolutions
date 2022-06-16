class Solution:
    def dfs(self, src, parent, visited, adj):
        visited[src] = True
        for i in adj[src]:
            if visited[i]==False:
                if self.dfs(i, src, visited, adj):
                    return True
            elif i!=parent:
                return True
        return False
    
    #Function to detect cycle in an undirected graph.
    def isCycle(self, V, adj):
        visited = [False]*V
        for i in range(V):
            if visited[i]==False:
                f = self.dfs(i, -1, visited, adj)
                if f:
                    return True
        return False



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
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends