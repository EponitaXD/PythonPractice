"""
Dictionary Challenge
Write a function that counts word frequencies in a 
sentence, ignoring case and punctuation. Return the 
top 3 words by frequency.

top_words("IBM is great, and IBM Consulting is growing!")
 → [("ibm", 2), ("is", 2), ("great", 1)]
"""

def top_words(s):
    # get substrings
    substrings = s.split(" ")
    print(f"subs: {substrings}")

    frequency = {}
    # loop thruogh them
    for word in substrings:
        # insert tupples in array
        if word.lower() not in frequency:
            frequency[word.lower()] = 1
        else:
            frequency[word.lower()] += 1

    print(f"freq: {frequency}")

    # sort dict values
    sorted_f = sorted(frequency.items(), key = lambda item: item[1], reverse=True)

    print(f"sorted: {sorted_f}")

    top_3 = []
    for i in range(0,3):
        top_3.append(sorted_f[i])

    return top_3

print(top_words("IBM is great, and IBM Consulting is growing!"))