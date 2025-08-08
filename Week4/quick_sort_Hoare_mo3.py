import sys
sys.setrecursionlimit(10000)  # Set recursion limit for large inputs

# Global counter for runtime analysis
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
    # No need to move the median to the end in Hoare's scheme
    return mid

def hoare_partition(A, low, high):
    """Partitions the array using Hoare's Partition Scheme."""
    global counter
    pivot_index = median_of_three(A, low, high)  # Use median-of-three to select pivot
    pivot = A[pivot_index]  # Use the median as the pivot
    i, j = low - 1, high + 1

    while True:
        # Move i to the right until an element >= pivot is found
        while True:
            counter += 1  # Count the comparison
            i += 1
            if A[i] >= pivot:
                break

        # Move j to the left until an element <= pivot is found
        while True:
            counter += 1  # Count the comparison
            j -= 1
            if A[j] <= pivot:
                break

        if i >= j:
            return j  # Return the partition index

        A[i], A[j] = A[j], A[i]  # Swap elements

def quicksort(A, low, high):
    """Quicksort implementation using Hoare's partition scheme and median-of-three."""
    if low < high:
        partition_index = hoare_partition(A, low, high)  # Partition the array
        quicksort(A, low, partition_index)  # Sort the left subarray
        quicksort(A, partition_index + 1, high)  # Sort the right subarray

# Example Usage
if __name__ == "__main__":
    test_array = [15, 3, 9, 8, 20, 7, 11, 4, 1, 13, 18, 5, 12]
    quicksort(test_array, 0, len(test_array) - 1)
    print("Sorted array:", test_array)
    print("Number of comparisons (counter):", counter)
