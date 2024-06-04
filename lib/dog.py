#!/usr/bin/env python3


APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    APPROVED_BREEDS = ["Labrador", "Golden Retriever", "Bulldog"]

    def __init__(self, name, breed=None):
        if not isinstance(name, str) or len(name) < 1 or len(name) > 25:
            print("Name must be string between 1 and 25 characters.")  # Print the error message
            raise ValueError("Name must be string between 1 and 25 characters.")
        self.name = name.title()
        if breed and breed not in self.APPROVED_BREEDS:
            print("Breed must be in list of approved breeds.")  # Print the error message
            raise ValueError("Breed must be in list of approved breeds.")
        self.breed = breed

