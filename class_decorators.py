# Assignment 17: Class Decorators
def add_greeting(cls):
    cls.greet = lambda self: "Hello from Decorator!"
    return cls

@add_greeting
class Person:
    pass

# Example usage
person = Person()
print(person.greet())  # Output: Hello from Decorator!