"""
List Manipulation
Given a list of integers, remove duplicates without 
using set(), and return the list in the order they 
first appear.

remove_duplicates([1,2,2,3,1,4])  # → [1,2,3,4]
"""

def remove_duplicates(my_array):
    final = []
    # loop through array
    for element in my_array:
        # if element is not in final append
        if element not in final:
            final.append(element)

    return final

no_duplicates = remove_duplicates([1,2,2,3,1,4])

print(no_duplicates)