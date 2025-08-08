import time
from Heap import heap

# Read input list
A = list(map(int, input().split()))

n = len(A)

st = time.process_time()

# Create a max heap with the input list
pq = heap(items=A, cmp=heap.maxCompare)

# Extract max elements and place them at the end of the list
for i in range(n-1, -1, -1):
    A[i] = pq.extract()

et = time.process_time()

print("Sorted List: ", A)
print("Time: ", et-st)