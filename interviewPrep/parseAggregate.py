data = [
    {"user": "A", "hours": 5},
    {"user": "B", "hours": 3},
    {"user": "A", "hours": 2},
]

# Return: {"A": 7, "B": 3}

result = {}

for element in data:
    # if the user is a key in result, we add the hours
    # if the user is not a key we create the key.
    if element["user"] in result.keys():
        result[element["user"]] += element["hours"]
    else:
        result[element["user"]] = element["hours"]

# print report
print(result)