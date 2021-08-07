# Write a function that takes in an array and returns a reversed array.
# don't use built-in reverse function. 

def reverse_array_in_place(arr):

    # midpoint is first of second chunk and center for odd items
    midpoint = len(arr)//2
    j = len(arr) - 1


    for i in range(len(arr[:midpoint])): # in range(2) # 1
        arr[i], arr[j] = arr[j], arr[i] #arr[1], arr[3] = arr[3], arr[1]
        
        j -= 1
    
    return arr



print(reverse_array_in_place([0, 1, 2, 3])) # even number items
# [3, 2, 1, 0]

print(reverse_array_in_place([0, None, "2", [1, 2]])) # non-digits
# [[1, 2], "2", None, 0]


print(reverse_array_in_place([]))
# []

print(reverse_array_in_place([1])) # one digit
# [1]

print(reverse_array_in_place([0, 1, 2, 3, 4])) # odd number of digits