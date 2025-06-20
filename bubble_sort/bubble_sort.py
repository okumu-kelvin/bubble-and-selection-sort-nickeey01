def bubble_sort(unsorted_list):
    n = len(unsorted_list)
    for i in range(n):
        for j in range(0, n - 1):
            if unsorted_list[j] > unsorted_list[j + 1]:
                unsorted_list[j], unsorted_list[j + 1] = unsorted_list[j + 1], unsorted_list[j]
    return unsorted_list

# Test the function (outside the bubble_sort function)
sorted_list = bubble_sort([30, 87, 16, 25, 12, 42])
print(sorted_list)