# Assignment 14: Aggregation
class Department:
    def __init__(self, name, employee):
        self.name = name
        self.employee = employee  # Aggregating employee object

class Employee:
    def __init__(self, name):
        self.name = name

# Example usage
emp = Employee("John")
dept = Department("HR", emp)
print(dept.employee.name)  # Output: John