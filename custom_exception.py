# Assignment 20: Creating a Custom Exception
class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18 or older")

# Example usage
try:
    check_age(16)
except InvalidAgeError as e:
    print(e)  # Output: Age must be 18 or older