class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        nr = len(matrix)
        nc = len(matrix[0])
        mdata = [nc, nr-1]
        mdir  = [[0,1],[1,0],[0,-1],[-1,0]]
        count = 0
        i , j = 0, -1

        while mdata[count%2]:
            for _ in range(mdata[count%2]):
                i += mdir[count][0]
                j += mdir[count][1]
                ans.append(matrix[i][j])
            mdata[count%2] = mdata[count%2] - 1
            count = (count + 1) % 4
        
        return ans