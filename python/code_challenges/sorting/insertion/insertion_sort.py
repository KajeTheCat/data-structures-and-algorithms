def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i - 1
        temp = arr[i]
        while j >= 0 and temp < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = temp
    return arr


if __name__ == "__main_":
    arr = [6,3,9,10,41,30,12]
    insertion_sort(arr)
