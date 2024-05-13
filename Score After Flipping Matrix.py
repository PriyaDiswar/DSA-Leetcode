"""
You are given an m x n binary matrix grid.
A move consists of choosing any row or column and toggling each value in that row or column (i.e., changing all 0's to 1's, and all 1's to 0's).
Every row of the matrix is interpreted as a binary number, and the score of the matrix is the sum of these numbers.

Return the highest possible score after making any number of moves (including zero moves).

Example 1:
Input: grid = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
Output: 39
Explanation: 0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39

Example 2:
Input: grid = [[0]]
Output: 1
"""
class Solution(object):
    def matrixScore(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows,cols=len(grid),len(grid[0])
        for i in range(rows):
            if grid[i][0]==0:
                for j in range(cols):
                    grid[i][j]=0 if grid[i][j] else 1
        
        for i in range(cols):
            cnt_one=0
            for j in range(rows):
                cnt_one+=grid[j][i] 
            if cnt_one<(rows-cnt_one):
                for j in range(rows):
                    grid[j][i]=0 if grid[j][i] else 1

        res=0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]:
                    res+=2**(cols-j-1)
        return res
