# Assignment 21: Make a Custom Class Iterable
class Countdown:
    def __init__(self, start):
        self.start = start
        self.current = start

    def __iter__(self):
        return self  # Returning the iterator object itself

    def __next__(self):
        if self.current <= 0:
            raise StopIteration  # Stop when countdown reaches 0
        self.current -= 1
        return self.current + 1  # Return the current countdown value

# Example usage
countdown = Countdown(5)
for number in countdown:
    print(number)
