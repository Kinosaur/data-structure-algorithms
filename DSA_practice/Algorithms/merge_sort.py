def merge_sort(list):
    '''
    Sorts a list in ascending order
    Returns a new sorted list

    Divide: Find the midpoint of the list and divide into sublists
    Conquer: Sort the sublists created in the previous step
    Combine: Merge the sorted sublists created in the previous step

    Runs in overall O(n log n ) time
    '''

    if len(list) <= 1:
        return list

    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(list):
    '''
    Divide the unsorted list at midpoint into sublists.
    Returns two sublists - left and right.

    Runs in overall O(n) time
    '''
    mid = len(list) // 2  # Find the midpoint
    left = []  # Initialize the left sublist
    right = []  # Initialize the right sublist

    i = 0  # Iterator for the list
    while i < len(list):
        if i < mid:
            left.append(list[i])  # Add elements to the left sublist
        else:
            right.append(list[i])  # Add elements to the right sublist
        i += 1  # Move to the next index

    return left, right

def merge(left, right):
    '''
    Merges two lists (arrays), sorting them in the process
    Returns a new merged list

    Runs in overall O(n) time
    '''

    l = []
    i = 0 # indexs at left list
    j = 0 # indexs at right list

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1

    while i < len(left):
        l.append(left[i])
        i += 1

    while j < len(right):
        l.append(right[j])
        j += 1

    return l
    
def verify_sorted(lst):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True


alist = [54, 93, 16, 17, 77, 31, 44, 55, 20]
l = merge_sort(alist)
print(verify_sorted(alist))
print(verify_sorted(l))

