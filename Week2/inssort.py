import time

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# R = [17, 21, 26, 29, 36] # Existing reservations
# t = 33 # Add reservation
# k = 3

# def add_reservation(R, t, k):
#     n = len(R)
    
#     if t < 0 or (n > 0 and t < R[0]):
#         return "Invalid"
    
#     for i in range(n):
#         if abs(R[i] - t) < k:
#             return "Rejected"
        
#     R.append(t)
#     insertion_sort(R)
#     return R

# print(add_reservation(R, t, k))


a = list(map(int, input().split()))
st = time.process_time()
sorted_a = insertion_sort(a)
et = time.process_time()
print(sorted_a)
print(et - st)
