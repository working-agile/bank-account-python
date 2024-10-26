class BankAccount:
    def __init__(self, initial_balance, email_sender=None, transfer_fee=0):
        self.balance = initial_balance
        self.email_sender = email_sender
        self.transfer_fee = transfer_fee

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            self.email_sender.send_email_to_bank()
            raise InsufficientBalanceException("Insufficient balance to withdraw")
        self.balance -= amount

    def transfer(self, amount, receiver_account):
        self.withdraw(amount + self.transfer_fee)
        receiver_account.deposit(amount)

class InsufficientBalanceException(Exception):
    pass
