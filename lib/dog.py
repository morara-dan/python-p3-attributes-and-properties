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
    def __init__(self, name = "Dog", breed = "Mastiff"):
        if  (type(name) == str) and (len(name) >= 1 and len(name) <= 25):
            self.name = name.title()
        else:
            print("Name must be string between 1 and 25 characters.")

        if breed in APPROVED_BREEDS:
            self.breed = breed
        else:
            print("Breed must be in list of approved breeds.")
        

        pass
    pass
