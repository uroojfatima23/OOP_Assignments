# Assignment 8: The super() Function
class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

# Example usage
teacher = Teacher("Mr. Smith", "Math")
print(teacher.name)  # Output: Mr. Smith
print(teacher.subject)  # Output: Math