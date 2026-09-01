# 1. QUICK SORT
def quicksort(arr, low, high):
    if low < high:
        i = low
        j = high
        pivot = low
        
        while i < j:
            while (i < len(arr) and arr[i] <= arr[pivot]):
                i += 1
                
            while (arr[j] > arr[pivot]):
                j -= 1
                
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
                
        arr[j], arr[pivot] = arr[pivot], arr[j]
        
        quicksort(a, low, j-1)
        quicksort(a, j+1, high)

a = list(map(int, input("Enter numbers to sort: ").split(" ")))
n = len(a)
quicksort(a, 0, n-1)
print("arr sorted")
print(a)

# 2. MERGE SORT
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        
        merge_sort(left_half)
        merge_sort(right_half)
        
        i = j = k = 0
        
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
            
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
            
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
            
    return arr


if __name__ == "__main__":
    user_input = input("Enter numbers to sort separated by spaces: ")
    numbers = [int(x) for x in user_input.split()]
    merge_sort(numbers)
    print("arr sorted:")
    print(numbers)