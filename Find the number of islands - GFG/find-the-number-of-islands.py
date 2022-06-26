#User function Template for python3

from collections import namedtuple, deque

Location = namedtuple("Location", ["row", "column"])

class Solution:
    def numIslands(self, arr):
        if type(arr[0]) == int:
            num_columns = len(arr)
            num_rows = 1
            arr = [arr]
        else:
            num_rows = len(arr)
            num_columns = len(arr[0])
        visited = self.create_visit_tracker(num_rows, num_columns)
        num_islands = 0
        for i in range(num_rows):
            for j in range(num_columns):
                if not visited[i][j] and arr[i][j] == 1:
                    num_islands += 1
                    visited[i][j] = True
                    self.find_island_tracker_iterative(arr, Location(i, j), visited) # start tracking a new island
                else:
                    visited[i][j] = True
        return num_islands

    def find_island_tracker_iterative(self, arr, location, visited):
        to_visit = deque()
        to_visit.append(location)
        while to_visit:
            location = to_visit.popleft()
            surrounding_blocks = [Location(location.row, location.column + 1), Location(location.row + 1, location.column + 1),
                                  Location(location.row + 1, location.column), Location(location.row - 1, location.column + 1),
                                  Location(location.row - 1, location. column), Location(location.row - 1, location.column - 1),
                                  Location(location.row + 1, location.column - 1), Location(location.row, location.column - 1)]
            surrounding_blocks = self.filter_out_visited_and_invalid(surrounding_blocks, len(arr), len(arr[0]), visited)
            for location in surrounding_blocks:
                if arr[location.row][location.column] == 1:
                    visited[location.row][location.column] = True
                    to_visit.append(location)
    
    def find_island_tracker(self, arr, location, visited):
        surrounding_blocks = [Location(location.row, location.column + 1), Location(location.row + 1, location.column + 1),
                              Location(location.row + 1, location.column), Location(location.row - 1, location.column + 1),
                              Location(location.row - 1, location. column), Location(location.row - 1, location.column - 1),
                              Location(location.row + 1, location.column - 1), Location(location.row, location.column - 1)]
        surrounding_blocks = self.filter_out_visited_and_invalid(surrounding_blocks, len(arr), len(arr[0]), visited)
        for location in surrounding_blocks:
            if arr[location.row][location.column] == 1:
                visited[location.row][location.column] = True
                self.find_island_tracker(arr, location, visited)
    
    
    def filter_out_visited_and_invalid(self, surrounding_blocks, num_rows, num_columns, visited):
        valid_locations = []
        for location in surrounding_blocks:
            if 0 <= location.row < num_rows and 0 <= location.column < num_columns and not visited[location.row][location.column]:
                valid_locations.append(location)
        return valid_locations
    
    
    def create_visit_tracker(self, rows, columns):
        return [[False for _ in range(columns)] for _ in range(rows)]

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n,m=map(int,input().strip().split())
        grid=[]
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])
        obj=Solution()
        print(obj.numIslands(grid))
# } Driver Code Ends