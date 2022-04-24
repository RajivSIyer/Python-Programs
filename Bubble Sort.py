def bubblesort(l):
    for i in range(len(l)-1, 0, -1):
        for j in range(1, i+1):
            if l[j-1] > l[j]:
                temp = l[j]
                l[j] = l[j-1]
                l[j-1] = temp
    return l

l = [5, 3, 1, 10, 7, 2, 4, 6, 9, 8]
print(bubblesort(l))

def bubblesort2(l):
    for i in range(len(l)-1):
        for j in range(1, len(l)):
            if l[j] < l[j-1]:
                temp = l[j-1]
                l[j-1] = l[j]
                l[j] = temp
    return l
l = [5, 3, 1, 10, 7, 2, 4, 6, 9, 8]
print(bubblesort2(l))
