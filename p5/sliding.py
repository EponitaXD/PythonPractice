"""
Sliding Window
Given an array and an integer k, return the maximum 
sum of any contiguous subarray of length k.
"""

def max_subarray_sum(my_array, k):
    if k > len(my_array):
        return -1
    if k < 0:
        return -1
    
    max = my_array[0] + my_array[1] + my_array[2]
    for i in range(0, len(my_array)):
        if i+2 > len(my_array) - 1:
            break
        # calc sum
        sum = my_array[i] + my_array[i+1] + my_array[i+2]

        if sum > max:
            max = sum

    return max


print(max_subarray_sum([2,1,5,1,3,2], 3))  # → 9 (5+1+3)