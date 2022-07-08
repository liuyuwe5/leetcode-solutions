class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        l = len(matrix[0])
        for row in matrix:
            if row[0] > target:
                print(">")
                break
            elif row[l-1] < target:
                print("<")
                continue
            else:
                for ele in row:
                    print(ele)
                    if ele == target:
                        return True
        
        return False