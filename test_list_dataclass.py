import json
from dataclasses import dataclass, field
from typing import List

@dataclass
class Person:
    name: str
    age: int
    friends: List['Person'] = field(default_factory=list)

    def add_friend(self, friend: 'Person'):
        if friend not in self.friends:
            self.friends.append(friend)
            from typing 
        else:
            print(f"{friend.name} is already a friend of {self.name}")

    def print_friends(self):
        for friend in self.friends:
            print(f"Name: {friend.name}, Age: {friend.age}")

    @classmethod
    def load_from_json(cls, file_path, instance):
        with open(file_path, 'r') as file:
            data = json.load(file)
            for person_data in data:
                friend = cls(**person_data)
                instance.add_friend(friend)

# Example of loading persons from a JSON file
file_path = 'D:\OneDrive\Documents\Emmanuel\Python\persons.json'
alice = Person("Alice", 30)

# Add persons from the JSON file to Alice's friends directly
Person.load_from_json(file_path, alice)

# Print Alice's friends
alice.print_friends()
