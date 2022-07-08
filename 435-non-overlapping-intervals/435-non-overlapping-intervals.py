class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        sortedInt = sorted(intervals, key=lambda x: (x[0], x[1]))

        
        prev = sortedInt[0]
        i = 1
        cnt = 0
        while i < len(intervals):
            if sortedInt[i][0] == prev[0]:
                cnt += 1
                print(i)
                print(prev)
            elif prev[1] >= sortedInt[i][1]:
                cnt += 1
                prev = sortedInt[i]
            elif prev[1] > sortedInt[i][0]:
                cnt += 1
            else:
                prev = sortedInt[i]
            print(i)
            print(prev)
            i += 1
        return cnt