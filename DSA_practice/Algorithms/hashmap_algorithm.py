K = int(input("Enter K: "))
a = list(map(int, input("Enter array: ").split()))

import time

st = time.process_time()

found = False
seen = {}

for x in a:
    if x != 0 and K % x == 0:  # Ensure no division by zero
        y = K // x
        if y in seen:
            found = True
            break
    seen[x] = True

et = time.process_time()

if not found:
    print("No pair exists")
else:
    print(x, y)
print("Running time:", et - st)