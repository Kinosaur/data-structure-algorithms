import time

# A = list(map(int, input().split()))

A = [5, 8, 19, 30, 1]

n = len(A)

def checkoutMax(a, lastIndex=0):
    # Locate the position of max item
    # Replace the item at max position with the last item
    # Return value of max item
    
    maxIndex = 0
    for i in range(1, lastIndex+1):
        if a[i] > a[maxIndex]:
            maxIndex = i
    maxItem = a[maxIndex]
    print(f"maxItem: {maxItem}")
    a[maxIndex] = a[lastIndex]
    return maxItem

st = time.process_time()
    
for i in range(n-1, -1, -1):
    A[i] = checkoutMax(A, i)

et = time.process_time()

print("Sorted List: ", A)
print("Time: ", et-st)





