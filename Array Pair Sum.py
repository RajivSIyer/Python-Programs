'''def pair_sum1(arr, k):
    sum_arr = []
    arith = 0
    flag = True
    while flag:
        index1 = 0
        index2 = 0
        if len(arr) >= 2:
            for index1 in range(len(arr)+1):
                arith = k - arr[index1]
                for index2 in range(1, (len(arr)+1)):
                    if arith == arr[index2]:
                        sum_arr.append((arr[index1], arr[index2]))
                        arr.pop(index2)
                        arr.pop(index1)
                        break
                    else:
                        arr.pop(index1)
                        break
                break
            continue
        else:
            flag = False

    sortedlist = []

    for t in sum_arr:
        if t[0] > t[1]:
            sortedlist.append((t[1], t[0]))
        else:
            sortedlist.append(t)

    return (set(sortedlist), len(set(sortedlist)))'''

def pair_sum2(arr, k):
    sum_arr = set()
    arith = 0
    while len(arr) >= 2:
        index1 = 0
        index2 = 0
        arith = k - arr[index1]
        for index2 in range(1, len(arr)):
            if arith == arr[index2]:
                sum_arr.add((min(arr[index1], arr[index2]), max(arr[index1], arr[index2])))
                arr.pop(index2)
                break
        arr.pop(index1)
    print(sum_arr)   
    return len(sum_arr)

print(pair_sum2([1,4,3,2,2,3,1,8,9,10], 4))

def pair_sum3(arr,k):
    
    if len(arr)<2:
        return
    
    # Sets for tracking
    seen = set()
    output = set()
    
    # For every number in array
    for num in arr:
        
        # Set target difference
        target = k-num
        
        # Add it to set if target hasn't been seen
        if target not in seen:
            seen.add(num)
        
        else:
            # Add a tuple with the corresponding pair
            output.add( (min(num,target),  max(num,target)) )
    
    
    # FOR TESTING
    return len(output)
    # Nice one-liner for printing output
    #return '\n'.join(map(str,list(output)))
