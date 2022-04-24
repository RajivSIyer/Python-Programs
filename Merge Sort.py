def merge_sort(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]

    return result

def mergesplit(l):
    if len(l) <= 1:
        return l
    mid = len(l)//2
    left = l[:mid]
    right = l[mid:]
    left = mergesplit(left)
    right = mergesplit(right)
    return merge_sort(left, right)

l = [5, 3, 1, 10, 7, 2, 4, 6, 9, 8]
print(mergesplit(l))