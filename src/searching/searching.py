def linear_search(arr, target):
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i 
    return -1   # not found

# test it

arr = [2, 6, 3, 8, 4, 55, 23, 44, 14, 8]
print(linear_search(arr, 8))


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1 
    while low <= high:
        middle = (high + low) // 2
        if target == arr[middle]:
            return middle
        elif target < arr[middle]:
            high = middle - 1
        else:
            # target > arr[middle]:
            low = middle + 1 
    return -1 

# test it

arr = [3,4,6,16,26,28,52,55]    
print(binary_search(arr, 4))  # worked, returned index of 1 where 4 is at
print(binary_search(arr, 52)) # worked, returned index of 6 where 52 is at
print(binary_search(arr, 8))  # worked, returned -1 since 8 not in list
print(binary_search(arr, 6))
