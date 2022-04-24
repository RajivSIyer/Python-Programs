def LCS1(arr):
    sumlist = [len(arr)*[] for i in range(len(arr))]
    print(sumlist)
    startindex = 0
    maxindex = 0
    maxsubindex = 0
    maxnum = 0
    stopindex = 0
    for i in range(len(arr)):
        total = 0
        sumlist[i] = [] 
        for j in range(i,len(arr)):
            total += arr[j]
            sumlist[i].append(total)
            if total > maxnum:
                maxnum = total
                maxindex = i
                maxsubindex = len(sumlist[i])-1
                stopindex = j
                startindex = j-maxsubindex

    print(sumlist)
    print(maxindex)
    print(maxsubindex)
    print('Maximum Number= ',maxnum)
    print('Start Index= ',startindex)
    print('Stop Index= ', stopindex)

    return (maxnum, arr[startindex:(stopindex+1)]) 

def LCS2(arr):

    if len(arr) == 0:
        return 0

    max_sum = current_sum = arr[0]

    for num in arr[1:]:
        current_sum = max(current_sum+num, num)
        max_sum = max(current_sum, max_sum)
    return max_sum

arr = [1,2,-1,3,4,-1]
print(LCS1(arr))
arr = [1,2,-1,3,4,10,10,-10,-1]
print(LCS1(arr))
arr = [-1,1,-19,2,3,4,10,10,-10,-1]
print(LCS1(arr))
arr = [-1,1]
print(LCS1(arr))

arr = [1,2,-1,3,4,-1]
print(LCS2(arr))
arr = [1,2,-1,3,4,10,10,-10,-1]
print(LCS2(arr))
arr = [-1,1,-19,2,3,4,10,10,-10,-1]
print(LCS2(arr))
arr = [-1,1]
print(LCS2(arr))