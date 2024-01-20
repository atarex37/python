import json

# Define a list of dictionaries, each representing a person
persons_data = [
    {"name": "John", "age": 28},
    {"name": "Emily", "age": 22},
    {"name": "Michael", "age": 35},
    {"name": "Sophie", "age": 29}
]

# Specify the file path for the JSON file
json_file_path = 'D:\OneDrive\Documents\Emmanuel\Python\persons.json'

# Write the person data to the JSON file
with open(json_file_path, 'w') as json_file:
    json.dump(persons_data, json_file, indent=2)

print(f"JSON file '{json_file_path}' created successfully.")
