def linear_search(a, item):
    for i in range(len(a)):
        if a[i] == item:
            print("Item found at index:", i)
            return 
    print("Item not found")

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
item = 6
linear_search(a, item)
