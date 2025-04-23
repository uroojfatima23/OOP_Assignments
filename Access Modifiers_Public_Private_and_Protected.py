# Assignment 7: Access Modifiers: Public, Private, and Protected
class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name  # public
        self._salary = salary  # protected
        self.__ssn = ssn  # private

# Example usage
emp = Employee("Urooj", 50000, "123-45-6789")
print(emp.name)  # Accessing public variable
print(emp._salary)  # Accessing protected variable (not recommended)
# print(emp.__ssn)  # This will throw an error because it's private