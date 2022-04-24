#lambda = numberofitems/tablesize

class mydictionary(object):
    def __init__(self):
        self.key = [None]*8
        self.value = [None]*8

    def gethashvalue(self, key, size):
        if key <= size:
            return key - 1
        else:
            hash = key % size
            return hash - 1

    def rehashval(self, oldhashval, key, size):
        
        newhashval = oldhashval
        while self.key[newhashval] != None and self.key[newhashval] != key and newhashval < size:
            newhashval += 1
        return newhashval

    def put(self, key, value):
        #for i in range(len(self.key)):
        hashvalue = self.gethashvalue(key, len(self.key))
        if key == self.key[hashvalue]:
            self.value[hashvalue] = value
        else: 
            #self.key.append(key)
            #self.value.append(value)
            if self.key[hashvalue] == None:
                self.key[hashvalue] = key
                self.value[hashvalue] = value
            else:
                print("Rehashing slots...")
                hashvalue = self.rehashval(hashvalue, key, len(self.key))
                if self.key[hashvalue] == None or self.key[hashvalue] == key:
                    self.key[hashvalue] = key
                    self.value[hashvalue] = value
                else:
                    print("No slots available.")

    def get(self, key):
        #for i in range(len(self.key)):
        hashvalue = self.gethashvalue(key, len(self.key))
        if key == self.key[hashvalue]:
            return self.value[hashvalue]
        else:
            hashvalue = self.rehashval(hashvalue, key, len(self.key))
            if key == self.key[hashvalue]:
                return self.value[hashvalue]
            else:
                print("Key not in dictionary.")
    
    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        return self.put(key, value)

    def __str__(self):
        s = '{'
        for i in range(len(self.key)):

            if type(self.key[i]) == str:
                k = "'" + self.key[i] + "'"
            else:
                k = self.key[i]
            if type(self.value[i]) == str:
                v = "'" + self.value[i] + "'"
            else:
                v = self.value[i]

            s += str(k) + ': ' + str(v)
            if i != len(self.key) - 1:
                s += ', '
        s += '}'
        return s

d = mydictionary()
#d['a'] = 1
#d['b'] = 2
#d['c'] = 3
d[1] = 'a'
d[3] = 'c'
d[5] = 'e'
d[8] = 'h'
print(d)
print(d[2])
d[2] = 'x'
print(d)
d[9] = 'z'
print(d)
d[9] = 'z'
print(d)
d[9] = 'y'
print(d)
d[29] = 'q'
print(d)
print(d[29])