# Assignment 6: Constructors and Destructors
class Logger:
    def __init__(self):
        print("Object created!")

    def __del__(self):
        print("Object destroyed!")

# Example usage
logger = Logger()
del logger  # Output: Object destroyed!