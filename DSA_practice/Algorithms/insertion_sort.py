import time

def insertion_sort(arr):
    st = time.process_time()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

    et = time.process_time()
    print("Running time:", et-st)
    
    return arr

print(insertion_sort([3,1,3,6,7,10,2]))

