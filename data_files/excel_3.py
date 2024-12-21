import csv
from pathlib import Path

# Write data to CSV
path = Path(__file__).parent.joinpath("data.csv")
data = [["Name", "Age", "City"], ["Alice", 25, "New York"], ["Bob", 30, "Los Angeles"]]
with path.open("w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)
    writer.writerow(["Charlie", 35, "Chicago"])
print("CSV file created.")

# Read data from CSV
with path.open("r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# Append data to CSV
new_data = ["David", 40, "Houston"]
with path.open("a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(new_data)
print("CSV file updated.")
