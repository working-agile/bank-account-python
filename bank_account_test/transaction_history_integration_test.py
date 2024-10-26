from unittest.mock import Mock
from bank_account import TransactionHistoryInMemory
from bank_account import BankAccount

def test_return_the_bank_statement_with_in_memory_transaction_history():
    # Given
    email_sender_dummy = Mock()
    transaction_history = TransactionHistoryInMemory()
    bank_account = BankAccount(1000, email_sender_dummy, transaction_history)
    bank_account.deposit(50)
    bank_account.withdraw(10)
    bank_account.deposit(100)
    bank_account.withdraw(1)
    bank_account.withdraw(2)

    # When
    bank_statement = bank_account.get_bank_statement()

    # Then
    assert bank_statement == "balance:1137,transactionHistory:[deposit:50,withdrawal:10,deposit:100,withdrawal:1,withdrawal:2]"