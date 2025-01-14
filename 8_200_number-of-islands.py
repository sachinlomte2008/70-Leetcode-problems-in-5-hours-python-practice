class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        ans = 0
        vis = set()
        gdir = [[0,1],[1,0],[0,-1],[-1,0]]
        nr = len(grid)
        nc = len(grid[0])

        def bfs(r,c):
            q = deque()
            q.append((r,c))
            vis.add((r,c))

            while q:
                ir, ic = q.popleft()
                for k,l in gdir:
                    i = ir + k
                    j = ic + l
                    if 0 <=i<nr and 0<=j<nc and grid[i][j]=='1' and (i,j) not in vis:
                        q.append((i,j))
                        vis.add((i,j))

        for i in range(nr):
            for j in range(nc):
                if grid[i][j] == '1' and (i,j) not in vis:
                    ans += 1
                    bfs(i, j)

        return ans