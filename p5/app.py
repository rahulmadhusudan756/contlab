import csv
with open("student.csv","r") as f:
    students = [(row["name"],int(row["marks"])) for row in csv.DictReader(f)]

for name,mark in students:
    print(name," | ")
    print("\u2588"*(mark//2),mark)