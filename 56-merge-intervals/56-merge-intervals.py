class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
       
        i = 1
        intervals=sorted(intervals, key=lambda x: x[0])
        res = [intervals[0]]
        ptr = 0
        while i < len(intervals):
            if res[ptr][1] >= intervals[i][1]:
                i += 1
            elif res[ptr][1] >= intervals[i][0]:
                new = [res[ptr][0],intervals[i][1]]
                res[ptr] = new
                i += 1
            else: 
                res.append(intervals[i])
                ptr +=1
                i += 1
                
        
        return res