def merge_two_sorted_lists(a, b, arr): #left, right, arr
    sorted_list = []
    len_a = len(a)   
    len_b = len(b)   
    i = j = k = 0
    
    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            arr[k] = a[i]
            i += 1
        else:
            arr[k] = b[j]
            j += 1
        k += 1
    
    while i < len_a:
        arr[k] = a[i]
        i += 1
        k += 1
        
    while j < len_b:
        arr[k] = b[j]
        j += 1
        k += 1

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    
    left = arr[:mid]
    right = arr[mid:]
    
    merge_sort(left)
    merge_sort(right)
    
    merge_two_sorted_lists(left, right, arr)

if __name__ == "__main__":
    tests = [
        [10, 3, 15, 7, 8, 23, 98, 29],
        [],
        [3],
        [9, 8, 7, 2],
        [1, 2, 3, 4, 5]
    ]
    
    for test in tests:
        merge_sort(test)
        print(f"Sorted Araary:", test)