import pytest
from unittest.mock import Mock
from bank_account import BankAccount, InsufficientBalanceException

def test_overdraft_should_trigger_email():
    # Arrange (Given)
    fake_email_sender = Mock()
    bank_account = BankAccount(1000, fake_email_sender)

    # Act (When)
    with pytest.raises(InsufficientBalanceException):
        bank_account.withdraw(1100)

    # Assert (Then)
    fake_email_sender.send_email_to_bank.assert_called_once()
    