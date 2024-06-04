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
    APPROVED_JOBS = ["Doctor", "Engineer", "Teacher", "ITC"]

    def __init__(self, name, job=None):
        if not isinstance(name, str) or len(name) < 1 or len(name) > 25:
            print("Name must be string between 1 and 25 characters.")  # Print the error message
            raise ValueError("Name must be string between 1 and 25 characters.")
        self.name = name.title()
        if job and job not in self.APPROVED_JOBS:
            print("Job must be in list of approved jobs.")  # Print the error message
            raise ValueError("Job must be in list of approved jobs.")
        self.job = job

