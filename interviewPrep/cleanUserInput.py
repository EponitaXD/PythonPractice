import string

def clean_text(text):
    # lowercase, remove punctuation
    # Question: do I remove whitespace? Nope
    # assume text is a string
    
    # to lower
    lower = text.lower()

    # Create a translation table:
    # the first two arguments are empty (no character mapping),
    # the third argument specifies characters to be deleted (mapped to None)
    translator = str.maketrans('', '', string.punctuation)
    # Use the translate method to remove the characters
    return lower.translate(translator)

# print report
print(clean_text("YOLO!!!!!!!! $%^# 8W*"))