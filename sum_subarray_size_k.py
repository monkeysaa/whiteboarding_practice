def max_sum_subarray_size_k(arr, k):
    """Find the maximum sum of any contiguous subarray of size 'k'.
    
    Given an array of positive numbers and a positive number ‘k,’ find the 
    maximum sum of any contiguous subarray of size ‘k’.

    Using sliding windows, set up a for loop tracking window_end. 
    use i for window-start
    Sum values
    Once subarray is length k (window-end = k-1), 
        begin dropping the value just behind window (window-start)
        max_sum = max(curr_sum, max_sum)
        window start += 1
    """

    max_sum = 0
    window_start = 0

    for window_end in range(len(arr)):
        window_sum += arr[window_end]

        if window_end >= k-1:
            max_sum = max(max_sum, window_sum)
            window_sum -= arr[window_start]
            window_start += 1

        


print(max_sum_subarray_size_k([2, 1, 5, 1, 3, 2], 3))
# 9, for subarray [5, 1, 3]
print(max_sum_subarray_size_k([2, 3, 4, 1, 5], 2))
# 7 for subarray [3, 4]
