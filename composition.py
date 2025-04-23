# Assignment 13: Composition
class Engine:
    def start_engine(self):
        print("Engine started!")

class Car:
    def __init__(self, engine):
        self.engine = engine

    def start(self):
        self.engine.start_engine()

# Example usage
engine = Engine()
car = Car(engine)
car.start()  # Output: Engine started!