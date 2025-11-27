class BankAccount:
    def __init__(self, initial_balance=0):
        """
        Initialize a new bank account.
        initial_balance: starting amount of money in the account (default = 0)
        """
        self.__account_balance = initial_balance  # Encapsulated attribute

    def deposit(self, amount):
        """Add money to the account balance."""
        if amount > 0:
            self.__account_balance += amount

    def withdraw(self, amount):
        """
        Deduct money from the account if sufficient funds exist.
        Returns True if withdrawal succeeds, False otherwise.
        """
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Print the current account balance."""
        print(f"Current Balance: ${self.__account_balance}")
