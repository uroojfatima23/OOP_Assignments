# Assignment 12: Static Methods
class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

# Example usage
temp_f = TemperatureConverter.celsius_to_fahrenheit(25)
print(temp_f)  # Output: 77.0