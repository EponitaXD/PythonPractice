"""
CSV Processing (without pandas)
Given a CSV file with columns id,name,salary, write a function 
to return the average salary. Handle missing or invalid values 
gracefully.
"""

import csv

def average_salary(file):
    with open(file, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)

        total = 0
        count = 0
        for row in reader:
            total += float(row[2])
            count += 1
        
        avarage = total / count

        return avarage


file = "p6/input.csv"
print(average_salary(file))