# Quick Sort Algorithm with Median-of-Three Pivot Selection Strategy
# This program sorts a list of student grades in ascending order using the Quick Sort algorithm.
# The median-of-three strategy is employed to choose the pivot for improved performance.

# Function to find the median of three elements and move it to the end
def median_of_three(A, low, high):
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

# Function to partition the array around the pivot
def partition(A, low, high):
    median_of_three(A, low, high)  # Choose pivot using median-of-three
    pivot = A[high]  # Pivot is now at the end
    i = low - 1
    for j in range(low, high):
        if A[j] <= pivot:  # Swap if element is less than or equal to pivot
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[high] = A[high], A[i + 1]
    return i + 1

# Quick Sort function using recursion
def quicksort(A, low, high):
    if low < high:
        pivot_index = partition(A, low, high)
        quicksort(A, low, pivot_index - 1)  # Sort elements before the pivot
        quicksort(A, pivot_index + 1, high)  # Sort elements after the pivot

if __name__ == "__main__":
    try:
        # Prompt the user for input
        input_sequence = input("Enter a list of integers separated by spaces: ").strip()
        if not input_sequence:
            print("Input cannot be empty. Please provide a valid list of integers.")
        else:
            A = list(map(int, input_sequence.split()))
            low = 0
            high = len(A) - 1

            # Sort the array using Quick Sort
            quicksort(A, low, high)

            # Display the sorted array
            print("Sorted array:", A)
    except ValueError:
        print("Invalid input. Please enter a list of integers separated by spaces.")

# if __name__ == "__main__":
#     try:
#         A = list(map(int, input().split(" ")))
#         low = 0
#         high = len(A) - 1
#         quicksort(A, low, high)
#         print("Sorted array:", A)
#     except ValueError:
#         print("Invalid input. Please enter a list of integers separated by spaces.")