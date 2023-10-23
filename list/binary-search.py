def binary_search(a,item):
    left = 0
    right = len(a)-1
    while left <= right:
        middle = (left + right) // 2 
        if a[middle] == item:
            print("Item found at Index:", middle)
            break 
        elif a[middle] < item:
            left = middle + 1
        else:
            right = middle - 1
    else:
        print("Item not found")
        

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
item = 6

binary_search(a, item)