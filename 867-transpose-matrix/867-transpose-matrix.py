class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        l=[]
        k=[]
        i=0
        j=0
        while(j!=len(matrix[0])):
            k.append(matrix[i][j])
            if i==len(matrix)-1:
                j+=1
                i=0
                l.append(k)
                k=[]
            else:
                i+=1
        return l