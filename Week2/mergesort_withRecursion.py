def merge(A, p, q, r):
    # Create a temporary array to hold merged elements
    B = []
    i = p  # Start of the first half
    j = q + 1  # Start of the second half

    # Merge the two halves into B
    while i <= q and j <= r:
        if A[i] <= A[j]:
            B.append(A[i])
            i += 1
        else:
            B.append(A[j])
            j += 1

    # Add any remaining elements from the first half
    A[p:r + 1] = B + A[i:q + 1] + A[j:r + 1]

def mergesort_recursion(A, p, r):
    if p < r:  # Base case: Stop if the array has one or no elements
        q = (p + r) // 2  # Find the midpoint
        # Recursively sort the first half
        mergesort_recursion(A, p, q)
        # Recursively sort the second half
        mergesort_recursion(A, q + 1, r)
        # Merge the sorted halves
        merge(A, p, q, r)

a = list(map(int, input().split()))

import time

st = time.process_time()
mergesort_recursion(a, 0, len(a) - 1)  # Sort the array
et = time.process_time()

print(a)
print(et - st)
