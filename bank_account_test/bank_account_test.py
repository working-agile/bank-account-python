import pytest
from bank_account import BankAccount, InsufficientBalanceException

def test_deposit_increases_balance():
    # Arrange (Given)
    bank_account = BankAccount(1000)

    # Act (When)
    bank_account.deposit(200)

    # Assert (Then)
    assert bank_account.get_balance() == 1200

def test_withdraw_decreases_balance():
    # Arrange (Given)
    bank_account = BankAccount(1000)

    # Act (When)
    bank_account.withdraw(200)

    # Assert (Then)
    assert bank_account.get_balance() == 800

def test_overdrawing_not_allowed():
    # Arrange (Given)
    bank_account = BankAccount(1000)

    # Act (When) & Assert (Then)
    with pytest.raises(InsufficientBalanceException):
        bank_account.withdraw(1100)

    # Assert (Then)
    assert bank_account.get_balance() == 1000