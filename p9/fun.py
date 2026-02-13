def findMin(myArr):
    if len(myArr) <= 0:
        return -1
    
    min = myArr[0]

    for element in myArr:
        if element < min:
            min = element
    
    return min


def isConsecutiveFour(values):
    for i in range(0,len(values)):
        for j in range(0,len(values[0])):
            # check if there are elements around it
            around = []
            current = values[i][j]
            if i-1 >= 0 and i-1 < len(values):
                around.append(values[i-1][j]) # up
                if j-1 >= 0 and j-1 < len(values[0]):
                    around.append(values[i-1][j-1]) # right_up
                if j+1 >= 0 and j+1 < len(values[0]):
                    around.append(values[i-1][j+1]) # left up
            if i+1 >= 0 and i+1 < len(values):
                around.append(values[i+1][j]) # down
                if j-1 >= 0 and j-1 < len(values[0]):
                    around.append(values[i+1][j-1]) # left_down
                if j+1 >= 0 and j+1 < len(values[0]):
                    around.append(values[i+1][j+1]) #right down
            if j-1 >= 0 and j-1 < len(values[0]):
                around.append(values[i][j-1]) # right
            if j+1 >= 0 and j+1 < len(values[0]):
                around.append(values[i][j+1]) # left
            
            for element in around:
                if element == current:

    return values


values = [[0,1,2,3,4],
          [1,3,4,5,6],
          [3,3,3,3,5],
          [1,1,2,4,6]]

print(f"This value repeats: {isConsecutiveFour(values)}")


arr = [1,2,3,6,5]
print(f"{findMin(arr)}")