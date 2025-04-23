# Assignment 2: Using cls
class Counter:
    count = 0  # class variable to track object count

    def __init__(self):
        Counter.count += 1  # increment count on object creation

    @classmethod
    def display_count(cls):
        print(f"Number of objects created: {cls.count}")

# Example usage
obj1 = Counter()
obj2 = Counter()
Counter.display_count()  # Output: Number of objects created: 2