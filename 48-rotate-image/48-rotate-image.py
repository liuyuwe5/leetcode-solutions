class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        res = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(matrix[-j-1][i])
            res.append(row)
            
        for i in range(n):
            matrix[i] = res[i]