def count_pairs(arr):
    freq = {}
    total = 0
    
    # Store frequencies
    for i in range(len(arr)):
        left_side = arr[i] + pow(i+1, 2)
        freq[left_side] = freq.get(left_side, 0) + 1
    
    # Count matches
    for j in range(len(arr)):
        right_side = arr[j] - pow(j+1, 2)
        total += freq.get(right_side, 0)
            
    return total

n = int(input())
arr = list(map(int, input().split()))
print(count_pairs(arr))