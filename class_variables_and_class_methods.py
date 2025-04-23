# Assignment 4: Class Variables and Class Methods
class Bank:
    bank_name = "ABC Bank"  # class variable

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

# Example usage
print(Bank.bank_name)  # Output: ABC Bank
Bank.change_bank_name("XYZ Bank")
print(Bank.bank_name)  # Output: XYZ Bank
