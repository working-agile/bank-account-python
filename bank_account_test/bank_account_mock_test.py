import pytest
from unittest.mock import Mock
from bank_account import BankAccount, InsufficientBalanceException

def test_overdraft_should_trigger_email():
    # Arrange (Given)
    email_sender_mock = Mock()
    transaction_history_mock = Mock()
    bank_account = BankAccount(1000, email_sender_mock, transaction_history_mock)

    # Act (When)
    with pytest.raises(InsufficientBalanceException):
        bank_account.withdraw(1100)

    # Assert (Then)
    email_sender_mock.send_email_to_bank.assert_called_once()
    