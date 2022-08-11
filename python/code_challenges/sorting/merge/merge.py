def mergesort(lst):
    n = len(lst)
    if n > 1:
        mid = int(n//2)
        left = lst[0:mid]
        right = lst[mid:]
        mergesort(left)
        mergesort(right)
        merge(left, right, lst)
    return lst

def merge(left, right, lst):
    i = 0
    j = 0
    k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            lst[k] = left[i]
            i = i + 1
        else:
            lst[k] = right[j]
            j = j + 1
        k = k + 1

    while i < len(left):
        lst[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        lst[k] = right[j]
        j += 1
        k += 1

    return lst

lst = [8,4,23,42,16,15]

print(mergesort(lst))
