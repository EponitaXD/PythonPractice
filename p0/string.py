"""
String Processing
Write a function that takes a string and returns the most 
frequent character. If multiple characters have the same 
frequency, return the lexicographically smallest one.

most_frequent_char("ibm consulting")  # → "i"
"""

def most_frequent_char(s):
    # create a dic containing char and count
    chars = {}
    # loop through s
    for char in s:
        # update dic
        if not char in chars:
            chars[char] = 1
        else:
            chars[char] += 1

    print(f"{chars}")

    # get char with greater count
    max = 0
    same = []
    for char, count in chars.items():
        if count > max:
            max = count
            same = []
            same.append(char)
        elif count == max:
            same.append(char)
    
    print(same)
        
    # check for same count
    min = same[0]
    for char in same:
        if char < min:
            min = char
    
    return min

value = most_frequent_char("ibm consulting")

print(value)