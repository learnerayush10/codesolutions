#User function Template for python3
class Solution:
    def topological_sort(self, graph, u, visited, S):
        visited[u] = True
        for v in graph[u]:
            if not visited[v]:
                self.topological_sort(graph, v, visited, S)
        S.append(u)
        
    def minColour(self, N, M, mat):
        graph = [[] for _ in range(N)]
        rev = [[] for _ in range(N)]
        for v, u in mat:
            graph[u-1].append(v-1)
            rev[v-1].append(u-1)
            
        color = [1]*N
        S = []
        visited = [False]*N
        for u in range(N):
            if not visited[u]:
                self.topological_sort(graph, u, visited, S)
        
        for v in S[::-1]:
            for u in rev[v]:
                color[v] = max(color[v], color[u] + 1)
            
        
        return max(color)

        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, M = [int(x) for x in input().split()]
        mat = [[0]*2 for y in range(M)]
        for i in range(M):
            arr = input().split()
            mat[i][0] = int(arr[0])
            mat[i][1] = int(arr[1])
        
        ob = Solution()
        print(ob.minColour(N, M, mat))
# } Driver Code Ends