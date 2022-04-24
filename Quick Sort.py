def swap(a, b, l):
    if a!=b:
        tmp = l[a]
        l[a] = l[b]
        l[b] = tmp

def partition(start, end, l):
    pivot_index = start
    pivot_value = l[pivot_index]

    while start < end:
        while start < len(l) and l[start] <= pivot_value:
            start += 1

        while l[end] > pivot_value:
            end -= 1

        if start < end:
            swap(start, end, l)

    swap(pivot_index, end, l)

    return end   

def quicksort(start, end, l):
    if start < end:
        pivotindex = partition(start, end, l)
        quicksort(start, pivotindex-1, l)
        quicksort(pivotindex+1, end, l)
    return l
    
lst = [5, 3, 1, 10, 7, 2, 4, 6, 9, 8]
startindex = 0
endindex = len(lst) - 1
print(quicksort(startindex, endindex, lst))