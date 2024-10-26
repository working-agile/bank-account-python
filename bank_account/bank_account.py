class BankAccount:
    def __init__(self, initial_balance, email_sender=None, transaction_history=None, transfer_fee=0):
        self.balance = initial_balance
        self.email_sender = email_sender
        self.transaction_history = transaction_history
        self.transfer_fee = transfer_fee

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.inform_transaction('deposit', amount)

    def withdraw(self, amount):
        if amount > self.balance:
            self.email_sender.send_email_to_bank()
            raise InsufficientBalanceException()
        self.balance -= amount
        self.transaction_history.inform_transaction('withdraw', amount)

    def transfer(self, amount, receiver_account):
        self.withdraw(amount + self.transfer_fee)
        receiver_account.deposit(amount)

class InsufficientBalanceException(Exception):
    pass
