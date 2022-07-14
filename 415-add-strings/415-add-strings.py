class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        prev = 0
        cur = ""
        res = ""
        len1 = len(num1)
        len2 = len(num2)
    
        for i in range(1, len1+1):
            if i <= len2:
                #print("=============")
                #print(num1[-i])
                #print(num2[-i])
                digitsum = ord(num1[-i]) + ord(num2[-i]) + prev - 2*ord("0") 
                #print(digitsum)
                if digitsum >= 10:
                    prev = 1
                    cur = str(digitsum-10)
                else:
                    prev = 0
                    cur = str(digitsum)
            else:
                digitsum = ord(num1[-i]) +  prev - ord("0") 
                if digitsum >= 10:
                    prev = 1
                    cur = str(digitsum-10)
                else:
                    prev = 0
                    cur = str(digitsum)
            # print("digitsum: " + str(digitsum))
            #print("cur: " + str(cur))
            #print("res: " + str(res))
            res = cur + res
            #print(res)
             
                
        i += 1
        while i <= len2:
            #print(i)
            digitsum = ord(num2[-i]) + prev - ord("0") 
            if digitsum >= 10:
                prev = 1
                cur = str(digitsum-10)
            else:
                prev = 0
                cur = str(digitsum)
            res = cur + res
            i += 1
        if prev == 1:
            res = "1" + res
        return res