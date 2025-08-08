
def partition(A, p, r):  # Lomuto's partition scheme
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[r], A[i+1] = A[i+1], A[r]
    return i + 1

# Verification Program
def test_partition():
    """Test the partition function with different cases."""
    test_cases = [
        [4, 2, 7, 1, 3],  # General case
        [10, 20, 30, 40, 5],  # Case where pivot is the smallest element
        [5, 3, 2, 1, 10],  # Case where pivot is the largest element
        [3, 3, 3, 3, 3],  # Case with identical elements
    ]
    for i, case in enumerate(test_cases, start=1):
        print(f"Test Case {i}: Original Array: {case}")
        pivot_index = partition(case, 0, len(case) - 1)
        print(f"Partitioned Array: {case}")
        print(f"Pivot Index: {pivot_index}\n")

# Run the test
if __name__ == "__main__":
    test_partition()
