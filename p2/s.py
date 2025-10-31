def getMinimumValue(data, maxOperations):
    # Write your code here
    # repeat maxOperations times
    # try each element combination and get the min difference
    # need to not take into accunts when the diff is from
    # the same element
    for i in range(0, maxOperations):
        mi = abs(data[0] - data[1])
        index0 = 0
        for element in data:
            index1 = 0
            for n in data:
                diff = abs(element - n)
                if diff < mi and not index0 == index1:
                    mi = diff
                index1 += 1
            index0 += 1
        # after going through all elements, append diff
        data.append(diff)
        
    return data[len(data)-1]

print(getMinimumValue([2,1,3], 2))