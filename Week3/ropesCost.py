import time
from Heap import heap

def minimum_rope_connection_cost(ropes):

    # Use default a min heap
    pq = heap(items=ropes)
    
    total_cost = 0
    
    # Continue connecting ropes until only one rope remains
    while pq.heapsize > 1:
        # Extract the two shortest ropes
        rope1 = pq.extract()
        rope2 = pq.extract()
        
        # Connect the ropes
        connected_rope = rope1 + rope2
        total_cost += connected_rope
        
        # Insert the connected rope back into the heap
        pq.insert(connected_rope)
    
    return total_cost

# Input: sequence of rope lengths separated by space
ropes = list(map(int, input().split()))

# Start time tracking
st = time.process_time()

# Calculate minimum rope connection cost
min_cost = minimum_rope_connection_cost(ropes)

# End time tracking
et = time.process_time()

# Print results
print("Minimum Total Cost: ", min_cost)
print("Time: ", et-st)