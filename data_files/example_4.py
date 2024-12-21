import json
from pathlib import Path

# Write data to JSON
data = {
    "users": [
        {"name": "Alice", "age": 25},
        {"name": "Bob", "age": 30},
    ]
}
path = Path(__file__).parent.joinpath("data.json")
test = json.dumps(data, indent=4)
print(test)
print(type(test))
test = json.loads(test)
print(test)
print(type(test))
with path.open("w") as file:
    json.dump(data, file, indent=4)
print("JSON file created.")

# Read data from JSON
with path.open("r") as file:
    data = json.load(file)
    print(data)

# Update JSON data
data["test"] = {"name": "Charlie", "age": 35}
data["users"].append({"name": "David", "age": 40})
with path.open("w") as file:
    json.dump(data, file, indent=4)
print("JSON file updated.")
