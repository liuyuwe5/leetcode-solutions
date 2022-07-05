class MyHashMap(object):
    hashMap = []

    def __init__(self):
        MyHashMap.hashMap = []

        
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        for i in range(len(MyHashMap.hashMap)):
            if MyHashMap.hashMap[i][0] == key:
                MyHashMap.hashMap[i] = [key, value]
                return
            
        MyHashMap.hashMap.append([key, value])
        return
    
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        for i in MyHashMap.hashMap:
            if i[0] == key:
                return i[1]
        return -1

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        for i in MyHashMap.hashMap:
            if i[0] == key:
                MyHashMap.hashMap.remove(i)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)