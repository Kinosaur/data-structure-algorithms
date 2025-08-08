# Longest Decreasing Subsequence (LDS) Problem
# This program finds the length of the longest decreasing subsequence in a given sequence of integers.
# For example:
# Input: 50 3 10 7 40 80
# Output: 3 (The LDS is [50, 10, 7])
#Input -> -12 24 -8 9 -1 0 -2 5 -5 , Output - 5

from bisect import bisect_left

def find_longest_decreasing_subsequence(arr):
    if not arr:
        return 0, []

    n = len(arr)
    # Negate elements to transform the problem into LIS (Longest Increasing Subsequence)
    neg_arr = [-x for x in arr]

    # Arrays to store LDS information
    tail = []  # Tracks the smallest ending element of each LDS length
    indices = []  # Tracks the indices of elements in the LDS
    prev = [-1] * n  # Tracks the previous element for each element in the LDS

    for i, num in enumerate(neg_arr):
        # Find the position where `num` should go in the `tail` array
        pos = bisect_left(tail, num)

        # Update or extend the LDS
        if pos < len(tail):
            tail[pos] = num
            indices[pos] = i
        else:
            tail.append(num)
            indices.append(i)

        # Update the predecessor index
        if pos > 0:
            prev[i] = indices[pos - 1]

    # Reconstruct the LDS
    lds = []
    current = indices[-1]
    while current != -1:
        lds.append(arr[current])  # Append original (non-negated) value
        current = prev[current]

    lds.reverse()  # Reverse to get the correct order
    return len(lds), lds

if __name__ == "__main__":
    # Input from the user
    input_sequence = input("Enter a sequence of integers separated by spaces: ").strip()
    arr = list(map(int, input_sequence.split()))

    if not arr:
        print("Input cannot be empty. Please provide a sequence of integers.")
    else:
        length, lds = find_longest_decreasing_subsequence(arr)
        print("Length of the Longest Decreasing Subsequence:", length)
        print("The Longest Decreasing Subsequence is:", lds)
