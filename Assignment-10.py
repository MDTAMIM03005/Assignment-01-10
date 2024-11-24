# Define the BankAccount class
class BankAccount:
    # The __init__ method initializes the account with a starting balance
    def __init__(self, balance):
        self.__balance = balance  # Private attribute __balance

    # Method to deposit an amount into the account
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount  # Increase the balance
        else:
            print("Deposit amount must be positive.")

    # Method to withdraw an amount from the account
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount  # Decrease the balance
        else:
            print("Insufficient funds for withdrawal.")

    # Method to get the current balance
    def get_balance(self):
        return self.__balance


# Sample input and operations
account = BankAccount(1000)  # Initialize the account with a balance of 1000
account.deposit(500)  # Deposit 500 into the account
print(account.get_balance())  # Print the current balance

account.withdraw(300)  # Withdraw 300 from the account
print(account.get_balance())  # Print the current balance

account.withdraw(1500)  # Try to withdraw 1500 (which exceeds the available balance)
