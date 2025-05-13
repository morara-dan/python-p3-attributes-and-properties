#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name = "Dan", job = "Finance"):
        if type(name) == str and (len(name) > 1 and len(name) < 25):
            self.name = name.title()
        else:
            print("Name must be string between 1 and 25 characters.")

        if job in APPROVED_JOBS:
            self.job = job
        else:
            print("Job must be in list of approved jobs.")
        

        pass
    pass
