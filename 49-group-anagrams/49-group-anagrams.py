class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for i in strs:
            key = ''.join(sorted(i))
            if key in dic:
                dic[key].append(i)
            else:
                dic[key] = [i]
            
        return list(dic.values())