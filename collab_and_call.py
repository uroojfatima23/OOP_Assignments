# Assignment 19: callable() and __call__()
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, number):
        return number * self.factor

# Example usage
multiplier = Multiplier(2)
print(callable(multiplier))  # Output: True
print(multiplier(5))  # Output: 10