#User function Template for python3
import sys

sys.setrecursionlimit(10**8)

class Solution:
    def minimum_amount (self, Edges, num, start, Cap):
        # code here
        # Recursive DFS function
        def recur(graph, visited, cur_node, Cap):
            if visited[cur_node]:
                return -1
                
            visited[cur_node] = True
            cur_cap = Cap[cur_node-1]
            max_neigh_cap = 0
            neighbours = 0
            
            for neigh_node in graph[cur_node]:
                neigh_cap = recur(graph, visited, neigh_node, Cap)
                if neigh_cap == -1:
                    continue
                max_neigh_cap = max(max_neigh_cap, neigh_cap)
                neighbours += 1
            
            cur_cap += max_neigh_cap * neighbours
            return cur_cap
            
        graph = {i: [] for i in range(1, num+1)}
        for n1, n2 in Edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
        
        visited = [False] * (num + 1)
        
        res = recur(graph, visited, start, Cap)
        for i in range(1, num+1):
            if not visited[i]:
                return -1
        if res > 10 ** 18:
            return -1
            
        return res



#{ 
#  Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        num, start = map(int,input().split())
        Cap = list(map(int, input().split()))
        Edges = list()
        for i in range(0, num-1):
            L = list(map(int, input().split()))
            Edges.append(L)
        ans = ob.minimum_amount(Edges, num, start, Cap);
        print(ans)




# } Driver Code Ends