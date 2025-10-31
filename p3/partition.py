# TODO: Permutations does not output all of the permutations. The rest needs to be tested

"""
Array Partitioning
Given an array of integers, split it into two 
subarrays with minimal difference in sum. Return 
the two subarrays.
"""

import itertools

def generate_permutations(arr):
  """
  Generates all permutations of the given array.

  Args:
    arr: The input array (list, tuple, or any iterable).

  Returns:
    A list of tuples, where each tuple represents a permutation.
  """
      
  return list(itertools.permutations(arr))


def partition_min_diff(arr):
    """
    Partition a list of non-negative integers `arr` into two lists (subset1, subset2)
    such that the absolute difference of their sums is minimal.
    Returns (subset1, subset2, diff).
    """
    # case 1: empty array
    if not arr:
        return [], [], 0

    # case 2: negative data
    if any(x < 0 for x in arr):
        raise ValueError("This implementation assumes non-negative integers.")

    # get permutations
    arrays = generate_permutations(arr)

    minArrs = []

    # calc first min
    sum0 = arrays[0][0]
    sum1 = sum(arrays[0][1:len(arrays[0])])
    min = abs(sum0-sum1)

    # slide the different elements calculating diff
        # store minimal arrays
    for a in arrays:
        for i in range(0,len(a)):
            # get sum of [0,i)
            arr0 = a[0:i]
            sum0 = sum(arr0)
            # get sum of [i,len-1]
            arr1 = a[i:len(a)]
            sum1 = sum(arr1)
            # get diff
            diff = abs(sum0-sum1)

            print(f"ARR0: {arr0}")
            print(f"ARR1: {arr1}")
            print(f"DIFF: {diff}")

            # if diff < min
            if diff < min:
                # empty subs array
                tempContainer = []
                minArrs = []

                # save current subs
                tempArr = []
                for i in range(0,len(arr0)):
                    tempArr.append(arr0[i])
                tempContainer.append(tempArr)

                tempArr = []
                for i in range(0,len(arr1)):
                    tempArr.append(arr1[i])
                tempContainer.append(tempArr)

                tempContainer.append(diff)
                minArrs.append(tempContainer)

                # min = diff
                min = diff

                print(f"added: {minArrs}")
            # elif diff = min
            elif diff == min:
                # append subs to subs array
                tempContainer = []

                # save current subs
                tempArr = []
                for i in range(0,len(arr0)):
                    tempArr.append(arr0[i])
                tempContainer.append(tempArr)

                tempArr = []
                for i in range(0,len(arr1)):
                    tempArr.append(arr1[i])
                tempContainer.append(tempArr)

                tempContainer.append(diff)

                minArrs.append(tempContainer)
                print(f"added: {minArrs}")
    
    return minArrs

"""
[1,6,11,5]
[[1],[6,11,5],diff], [[1,6],[11,5],diff], [1,6,11],[5],diff
[6,1,11,5]
[6],[1,11,5],diff, [6,1],[11,5],diff, [6,1,11],[5],diff
[6,11,1,5]
[6],[11,1,5],diff, [6,11],[1,5],diff, [6,11,1],[5],diff
[6,11,5,1]
[11,6,5,1]
[11,5,6,1]
[11,5,1,6]
[5,]
"""


arr = [1, 6, 11, 5]
minArrs = partition_min_diff(arr)
print("\nRESULTS:")
for element in minArrs:
    print("Partition")
    print(f"Sub0: {element[0]}")
    print(f"Sub1: {element[1]}")
    print(f"Diff: {element[2]}")