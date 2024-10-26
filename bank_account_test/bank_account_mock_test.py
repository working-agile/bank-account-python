import pytest
from bank_account import BankAccount, InsufficientBalanceException
from bank_account import FakeEmailSender

def test_overdraft_should_trigger_email():
    # Arrange (Given)
    fake_email_sender = FakeEmailSender()
    bank_account = BankAccount(1000, fake_email_sender)

    # Act (When)
    with pytest.raises(InsufficientBalanceException):
        bank_account.withdraw(1100)

    # Assert (Then)
    assert fake_email_sender.has_sent_email == True
    assert fake_email_sender.how_many_times_sent_email == 1
    