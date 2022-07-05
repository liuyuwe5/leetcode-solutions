class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        prev = [1]
        i = 0
        current = [1]
        while i<rowIndex:
            current =[1]
            j=0
            for j in range(len(prev)-1):
                current.append(prev[j]+prev[j+1])
            current.append(1)
            prev = current
            i += 1
            
        return current
        