def merge(A, p, q, r):
    B = []
    i = p
    j = q + 1
    while i <= q and j <= r:
        if A[i] <= A[j]:
            B.append(A[i])
            i += 1
        else:
            B.append(A[j])
            j += 1
    A[p:r + 1] = B + A[i:q + 1] + A[j:r + 1]

def mergesort_noRecursion(A, p, r):
    current_size = 1  # Start with subarrays of size 1

    # Continue until the entire array is sorted
    while current_size <= r - p:
        # Merge subarrays in pairs
        for start in range(p, r, 2 * current_size):
            mid = min(start + current_size - 1, r)  # End of the first half
            end = min(start + 2 * current_size - 1, r)  # End of the second half
            merge(A, start, mid, end)  # Merge the two halves

        current_size *= 2  # Double the size of subarrays for the next iteration

a = list(map(int, input().split()))

import time

st = time.process_time()
mergesort_noRecursion(a, 0, len(a) - 1)  # Sort the array
et = time.process_time()

print(a)
print(et - st)