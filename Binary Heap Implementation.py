class BinHeap(object):
    def __init__(self):
        self.HeapList = [0]
        self.CurrentSize = 0

    def Insert(self, k):
        self.HeapList.append(k)
        self.CurrentSize += 1
        self.PercUp(self.CurrentSize)
        print(self.HeapList)
        self.PrintTree()

    def PercUp(self, i):
        while i // 2 > 0:
            if self.HeapList[i] < self.HeapList[i // 2]:
                tmp = self.HeapList[i // 2]
                self.HeapList[i // 2] = self.HeapList[i]
                self.HeapList[i] = tmp
            i = i // 2

    def delmin(self):
        retval = self.HeapList[1]
        self.HeapList[1] = self.HeapList[self.CurrentSize]
        self.CurrentSize -= 1
        self.HeapList.pop()
        self.PercDown(1)
        print(self.HeapList)
        self.PrintTree()
        return retval

    def PercDown(self, i):
        while 2*i <= self.CurrentSize:
            mc = self.MinChild(i)
            if self.HeapList[i] > self.HeapList[mc]:
                tmp = self.HeapList[i]
                self.HeapList[i] = self.HeapList[mc]
                self.HeapList[mc] = tmp
            i = mc

    def MinChild(self, i):
        if 2*i+1 > self.CurrentSize:
            return 2*i
        else:
            if self.HeapList[2*i] < self.HeapList[2*i+1]:
                return 2*i
            else:
                return 2*i+1

    def BuildHeap(self, alist):
        i = len(alist) // 2
        self.HeapList = [0] + alist[:]
        self.CurrentSize = len(alist)
        while i > 0:
            self.PercDown(i)
            i -= 1

    def PrintTree(self):
        i = 1
        while 2*i <= self.CurrentSize:
            print('Index= ', i, 'Value= ', self.HeapList[i])
            if 2*i <= self.CurrentSize:
                print('Left Index= ', 2*i, 'Left Value= ', self.HeapList[2*i])
            if 2*i+1 <= self.CurrentSize:
                print('Right Index= ', 2*i+1, 'Right Value= ', self.HeapList[2*i+1])
                print('\n')
            i += 1  

b = BinHeap()
b.BuildHeap([9,6,5,3,2])
print(b.HeapList)
b.PrintTree()
b.Insert(1)
b.delmin()