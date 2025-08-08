import sys
sys.setrecursionlimit(10000)

counter = 0

def partition(A, p, r):
    global counter
    x = A[r]  # Pivot element
    i = p - 1
    for j in range(p, r):
        counter += 1  # Count the comparison
        if A[j] <= x:  # Compare with pivot
            i += 1
            A[i], A[j] = A[j], A[i]  # Swap
    A[r], A[i + 1] = A[i + 1], A[r]  # Place pivot in correct position
    return i + 1

def quicksort(A, low, high):
    if low < high:
        pivot_index = partition(A, low, high)  # Partition the array
        quicksort(A, low, pivot_index - 1)  # Recursively sort the left subarray
        quicksort(A, pivot_index + 1, high)  # Recursively sort the right subarray

# Input and execution
if __name__ == "__main__":
    A = list(map(int, input().split()))
    low = 0
    high = len(A) - 1
    quicksort(A, low, high)
    # print("Sorted array:", A)
    print("Number of comparisons (counter):", counter)
