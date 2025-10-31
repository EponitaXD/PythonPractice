"""
Implement a function that performs binary search on a sorted 
list without using built-in functions. Return the index of 
the target or -1 if not found.
"""

def binary_search(myArray, element):
    low = 0
    high = len(myArray) -1

    while low < high:
        mid = int((low + high) / 2)

        if myArray[mid] == element:
            return mid
        elif element > myArray[mid]:
            low = mid
        else:
            high = mid

    return -1

print(binary_search([1,3,5,7,9], 7))