def FME(arr1, arr2):
    dict1 = {}
    dict2 = {}
    for i in arr1:
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1

    for j in arr2:
        if j in dict2:
            dict2[j] += 1
        else:
            dict2[j] = 1

    while len(arr1) != len(arr2):
        for k1 in dict1:
            for k2 in dict2:
                if k2 == k1:
                    if dict2[k2] == dict1[k1]:
                        break
                    else:
                        arr2.append(k1)
                        break
            else:
                arr2.append(k1)
                break
            print('Exiting inner for loop')
        print('Exiting outer for loop')
    print('Exiting while loop')
    return (arr2)


def FME2(arr1, arr2):
    dict1 = {}
    dict2 = {}
    for i in arr1:
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1

    for j in arr2:
        if j in dict2:
            dict2[j] += 1
        else:
            dict2[j] = 1

    miss = []
    for k1 in dict1:
        if k1 not in dict2:
            miss.append(k1)
        else:
            if dict2[k1] != dict1[k1]:
                miss.append(k1)
    
    print('Exiting outer for loop')
    return (miss)

def FME3(arr1, arr2): #This method will work if only one element is missing
    arr1.sort()
    arr2.sort()

    for num1,num2 in zip(arr1,arr2):
        if num1 != num2:
            return num1
    
    return arr1[-1]

import collections

def FME4(arr1, arr2): #This method will work if only one element is missing

    d = collections.defaultdict(int)

    for num in arr2:
        d[num] += 1

    for num in arr1:
        if d[num] == 0:
            return num
        else:
            d[num] -= 1

arr1 = [1,2,3,4,5,6,7]
arr2 = [3,7,2,1,4,6]
print(FME2(arr1, arr2))
arr1 = [5,5,7,7]
arr2 = [5,5,7]
print(FME2(arr1, arr2))