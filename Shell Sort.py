def shellsort(l):
    sublistcount = int(len(l)/2) 
    while sublistcount > 0:
        for start in range(sublistcount):
            gap_insertion(l,start,sublistcount)
        sublistcount = int(sublistcount/2)

    return l

def gap_insertion(l, start, gap):
    for i in range(start+gap,len(l),gap):
        currentvalue = l[i]
        position = i
        while position >= gap and l[position-gap] > currentvalue:
            l[position] = l[position - gap]
            position = position - gap
        
        l[position] = currentvalue

l = [5, 3, 1, 10, 7, 2, 4, 6, 9, 8]
print(shellsort(l))