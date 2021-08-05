import requests


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def monthly_schedule(self, month):
        response = requests.get(f"https://company.com/{self.name}/{month}")
        if response.ok:
            return response.text
        else:
            return "Bad Response!"
