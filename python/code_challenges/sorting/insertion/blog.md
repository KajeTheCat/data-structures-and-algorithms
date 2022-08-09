# Insertion Sort Blog

## Pseudocode

  InsertionSort(int[] arr)

    FOR i = 1 to arr.length

      int j <-- i - 1
      int temp <-- arr[i]

      WHILE j >= 0 AND temp < arr[j]
        arr[j + 1] <-- arr[j]
        j <-- j - 1

      arr[j + 1] <-- temp

## Trace

Sample list: [8,4,23,42,16,15]

### Pass 1

In the first pass through of the insertion sort, we check if 4 is larger than 8. As it is, we move 4 to the left.

### Pass 2

In the second pass, we compare 8 to 23, and since 23 is larger than 8 we leave it where it is.

### Pass 3

In the third pass, we compare 23 to 42, since 23 is smaller than 42 we leave the numbers where they are.

### Pass 4

In the fourth pass we compare 16 to 42, 23, and 8. Since 16 is larger than 8 we move it down between 8 and 23.

### Pass 5

In the final pass, we compare 15 to 42, 23, 16, and 8. Since 15 is larger than 8 and smaller than 16, we move it down between these two values.

### 6

In this final pass, the code see's no more numbers inside our list and stops the code.

## Efficiency

+ Time: O(n)

+ Space: O(n)
