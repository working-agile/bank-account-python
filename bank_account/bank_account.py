class BankAccount:
    def __init__(self, initial_balance):
        self.balance = initial_balance

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientBalanceException()
        self.balance -= amount

class InsufficientBalanceException(Exception):
    pass
