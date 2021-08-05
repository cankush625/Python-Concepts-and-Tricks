class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @property
    def get_name(self):
        return self.name

    @property
    def get_email(self):
        return f"{self.name}@email.com"

    @property
    def get_salary(self):
        return self.salary

    def salary_hike(self):
        return self.salary * 1.05
