class TransactionHistoryInMemory:
    def __init__(self):
        self.transactions = []

    def inform_transaction(self, transaction, amount):
        if transaction == 'withdraw':
            amount = -amount
        self.transactions.append(amount)

    def get_transaction_history(self):
        return list(self.transactions)
    