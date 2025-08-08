import sys
sys.setrecursionlimit(10000)  # Set recursion limit for large inputs

# Global counter to track the number of comparisons in the partition function
counter = 0

def median_of_three(A, low, high):
    """Selects the median of the first, middle, and last elements as the pivot."""
    mid = (low + high) // 2
    # Order the first, middle, and last elements
    if A[low] > A[mid]:
        A[low], A[mid] = A[mid], A[low]
    if A[low] > A[high]:
        A[low], A[high] = A[high], A[low]
    if A[mid] > A[high]:
        A[mid], A[high] = A[high], A[mid]
    # Move the median to the end to simplify partition logic
    A[mid], A[high] = A[high], A[mid]

def partition(A, low, high):
    """Partitions the array around the pivot chosen by median_of_three."""
    global counter
    median_of_three(A, low, high)  # Choose pivot using median-of-three
    pivot = A[high]  # Pivot is now at the end
    i = low - 1
    for j in range(low, high):
        counter += 1  # Increment the counter for each comparison
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[high] = A[high], A[i + 1]  # Place pivot in correct position
    return i + 1

def quicksort(A, low, high):
    """Quicksort implementation using the median-of-three method."""
    if low < high:
        pivot_index = partition(A, low, high)  # Partition the array
        quicksort(A, low, pivot_index - 1)  # Sort the left subarray
        quicksort(A, pivot_index + 1, high)  # Sort the right subarray

# Input and execution
if __name__ == "__main__":
    A = list(map(int, input().split()))
    low = 0
    high = len(A) - 1
    quicksort(A, low, high)  # Perform QuickSort
    # print("Sorted array:", A)
    print("Number of comparisons (counter):", counter)
