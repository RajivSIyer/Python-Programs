'''
for i in range(1, 10):
    iteration 2 = 2
    currval = l[i] = l[2] = 1
    pos = i = 2
    while pos > 0 and l[pos-1] > currval: i.e 1 > 0 and 3 > 1
        l[pos] = l[pos - 1] i.e [3,(3),5,10,7,2,4,6,9,8]
        pos = pos - 1 = 2 - 1 = 1
    exit while
    l[pos] = currval i.e [(1),3,5,10,7,2,4,6,9,8]

'''
def insertionsort(l):
    for i in range(1, len(l)):
        currentvalue = l[i]
        position = i

        while position > 0 and l[position-1] > currentvalue:
            l[position] = l[position-1]
            position -= 1
        l[position] = currentvalue

    return l
    
l = [5, 3, 1, 10, 7, 2, 4, 6, 9, 8]
print(insertionsort(l))