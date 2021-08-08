def smallest_subarray_sum_S(arr, S):
    """Find the length of the smallest contiguous subarray with sum S or more.
    
    Given an array of positive numbers and a positive number ‘S,’ find the 
    length of the smallest contiguous subarray whose sum is greater than or equal 
    to ‘S’. Return 0 if no such subarray exists.
    """
    small_subarray = len(arr) + 1
    # could set to math.inf
    window_start = 0
    window_sum = 0
    
    for window_end in range(len(arr)):
        window_sum += arr[window_end]

        while window_sum >= S:
            small_subarray = min(small_subarray, window_end - window_start + 1)
            window_sum -= arr[window_start]
            window_start += 1
    
    if small_subarray == len(arr) + 1:
        return 0
    else:
        return small_subarray
    

print(smallest_subarray_sum_S([2, 1, 5, 2, 3, 2], 7))
# 2

print(smallest_subarray_sum_S([2, 1, 5, 2, 8], 7))
# 1

print(smallest_subarray_sum_S([3, 4, 1, 1, 6], 8))
# 3

