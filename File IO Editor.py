from os import path
from typing import Counter

class SingleLL(object):
    def __init__(self, filename):
        self.filename = filename
        self.head = None
        self.count = 0

    def linkwords(self):
        f = open(filename)
        string = f.read()
        lines = string.splitlines()
        previous = None
        words = []
        for l in lines:
            words += l.split()

        words = sorted(words, key=str.casefold)  
        for w in words:
            x = Node(w)
            if self.head == None:
                self.head = x
            if previous != None:
                previous.next = x
            previous = x
            self.count += 1
        f.close()

    def show(self):
        current = self.head
        if current != None:
            while current.next != None:
                print(current.word)
                current = current.next
            print(current.word)
        else:
            print("Error! Linked List is Empty.")

class Node(object):
    def __init__(self, word):
        self.word = word
        self.next = None

filename = 'Editor1.txt'

if path.exists(filename):
    f = open(filename, 'a+')
else:
    f = open(filename, 'w+')
while True:
    i = input("Give input: ")
    if i.lower() != 'bye':
        f.write(i+' ')
        f.seek(0,0)
        print(f.read())
        f.seek(0,2)
    else:
        break
f.close()

lnklst = SingleLL(filename)
lnklst.linkwords()
print(lnklst.count)
lnklst.show()