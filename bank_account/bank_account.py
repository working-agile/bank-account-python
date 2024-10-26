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

    def get_bank_statement(self):
        transaction_list = self.transaction_history.get_transaction_history() if self.transaction_history else []
        statement = f"balance:{self.balance},transactionHistory:"

        if not transaction_list:
            statement += "empty"
        else:
            statement += "["
            num_transactions = len(transaction_list)
            for i in range(num_transactions):
                amount = transaction_list[i]
                if amount >= 0:
                    statement += f"deposit:{amount}"
                else:
                    statement += f"withdrawal:{-amount}"
                if i < num_transactions - 1:
                    statement += ","
            statement += "]"
        
        return statement

class InsufficientBalanceException(Exception):
    pass
