class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]
        
    def get_hash(self, key):
        hash = 0
        for i in key:
            hash += ord(i)
            return hash % self.MAX
            
    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h] if self.arr[h] is not None else "Not Found"
        
    def __setitem__(self, key, value):
        h = self.get_hash(key)
        self.arr[h] = value
        
    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None
        
        
t = HashTable()
print (t.arr)
t["March 16"] = 120
t["Feb 20"] = 130
print(t.arr)
print(t["March 16"])
print(t["Feb 20"])
del t["Feb 20"]
print(t.arr)
print(t["Feb 20"])
