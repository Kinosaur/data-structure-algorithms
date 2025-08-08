def insertion_sort(elements, end):
    """Sorts the list in place up to the given index 'end'."""
    for i in range(1, end + 1):
        anchor = elements[i]
        j = i - 1
        
        while j >= 0 and anchor < elements[j]:
            elements[j + 1] = elements[j]
            j -= 1
        elements[j + 1] = anchor

def insertion_median(elements):
    for i in range(len(elements)):
        # Sort the portion of the list up to the current index
        insertion_sort(elements, i)
        
        # Current sorted sublist
        sorted_sublist = elements[:i + 1]
        length = len(sorted_sublist)
        
        if length % 2 == 0:  # Even length
            median = (sorted_sublist[length // 2 - 1] + sorted_sublist[length // 2]) / 2
        else:  # Odd length
            median = sorted_sublist[length // 2]
        
        print(median)

if __name__ == '__main__':
    exercise = [2, 1, 5, 7, 2, 0, 5]
    
    tests = [
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]
    
    for elements in tests:
        insertion_median(elements)
        print(f'sorted array: {elements}')