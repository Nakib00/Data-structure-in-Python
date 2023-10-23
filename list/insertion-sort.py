def insertion_sort(arr):
    for i in range(len(arr)):
        temp = arr[i]
        j = i-1
        while j>=0 and arr[j]>temp:
            arr[j+1] = arr[j]
            j -=1
        arr[j+1]=temp
    return arr

arr = [4,8,6,2,7,9,5]

print('Unsorted array',arr)

sorted = insertion_sort(arr)

print('Sorted array',sorted)