class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        mat = [[0 for i in range(n)] for j in range(n)]
   
        i = 0
        j = 0
        cnt = n-1
        incre = 1
        
        while cnt>0:
            for k in range(cnt):
                (mat[i])[j] = incre
                incre += 1
                j += 1
                print(mat)
            for k in range(cnt):
                mat[i][j] = incre
                incre += 1
                i += 1
                print(mat)
            for k in range(cnt):
                mat[i][j] = incre
                incre += 1
                j -= 1
                print(mat)
            for k in range(cnt):
                mat[i][j] = incre
                incre += 1
                i -= 1
                print(mat)
            print("cnt:" + str(cnt))
            i += 1
            j += 1
            cnt -= 2
            

        if incre == n*n:
            mid = int((n-1)/2)
            mat[mid][mid] = incre
    
   
        return mat
        