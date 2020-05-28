class Solution(object):
    def getMaximumGold(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.xLen=len(grid[0])
        self.yLen=len(grid)
        MaximumGold=0
        self.grid=grid
        for y in range(self.yLen):
            for x in range(self.xLen):
                tmp=self.DFS(y,x,0)
                if tmp > MaximumGold:
                    MaximumGold=tmp
        return MaximumGold
        
    def DFS(self, y, x, gold):
        if y >= self.yLen or x >= self.xLen or x  < 0 or y < 0 or self.grid[y][x]  <= 0:
            return gold
        self.grid[y][x]=-1*self.grid[y][x]
        tmp = max(self.DFS(y-1,x,gold-self.grid[y][x]),self.DFS(y+1,x,gold-self.grid[y][x]),self.DFS(y,x+1,gold-self.grid[y][x]),self.DFS(y,x-1,gold-self.grid[y][x]))
        self.grid[y][x]=-1*self.grid[y][x]
        return tmp              
        
sln=Solution()
assert 60==sln.getMaximumGold([[1,0,7,0,0,0],[2,0,6,0,1,0],[3,5,6,7,4,2],[4,3,1,0,2,0],[3,0,5,0,20,0]])
assert 24==sln.getMaximumGold(grid = [[0,6,0],[5,8,7],[0,9,0]])
assert 28==sln.getMaximumGold(grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]])
