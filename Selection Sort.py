def selectionsort(l):
    for lastindex in range(len(l)-1, 0, -1):
        positionofmax = 0
        for currentindex in range(1, lastindex+1):
            if l[currentindex] > l[positionofmax]:
                positionofmax = currentindex

        if positionofmax != lastindex:
            temp = l[lastindex]
            l[lastindex] = l[positionofmax]
            l[positionofmax] = temp

    return l


l = [5, 3, 1, 10, 7, 2, 4, 6, 9, 8]
print(selectionsort(l))