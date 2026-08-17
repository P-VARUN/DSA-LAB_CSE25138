# 1) WAP to implement linear search
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

my_array = [10, 23, 45, 70, 11, 15]
target_val = 70
print(linear_search(my_array, target_val))

# 2) WAP to implement binary search with and without sorted array as an inputWith a sorted array as input:
def binary_search_sorted(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1

sorted_array = [11, 22, 34, 45, 55, 67, 89]
target_val = 45
print(binary_search_sorted(sorted_array, target_val))


# Without a sorted array as an input (sorts the array first before searching):
def binary_search_unsorted(arr, target):
    arr.sort()
    
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1

unsorted_array = [67, 11, 89, 22, 55, 45, 34]
target_val = 45
print(binary_search_unsorted(unsorted_array, target_val))