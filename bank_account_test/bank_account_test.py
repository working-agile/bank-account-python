import pytest
from unittest.mock import Mock
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
    fake_email_sender = Mock()
    bank_account = BankAccount(1000, fake_email_sender)

    # Act (When) & Assert (Then)
    with pytest.raises(InsufficientBalanceException):
        bank_account.withdraw(1100)

    # Assert (Then)
    assert bank_account.get_balance() == 1000

def test_transfer_value_to_other_account():
    # Arrange (Given)
    bank_account_sender = BankAccount(1000)
    bank_account_receiver = BankAccount(0)

    # Act (When)
    bank_account_sender.transfer(500, bank_account_receiver)

    # Assert (Then)
    assert bank_account_sender.get_balance() == 500
    assert bank_account_receiver.get_balance() == 500

def test_transfer_amount_higher_than_balance():
    # Arrange (Given)
    fake_email_sender = Mock()
    bank_account_sender = BankAccount(1000, fake_email_sender)
    bank_account_receiver = BankAccount(0, fake_email_sender)

    # Act (When) & Assert (Then)
    with pytest.raises(InsufficientBalanceException):
        bank_account_sender.transfer(1100, bank_account_receiver)

    # Assert (Then)
    assert bank_account_sender.get_balance() == 1000
    assert bank_account_receiver.get_balance() == 0

def test_transfer_fee_is_charged():
    # Arrange (Given)
    transfer_fee = 10
    fake_email_sender = Mock()
    bank_account_sender = BankAccount(1000, fake_email_sender, transfer_fee)
    bank_account_receiver = BankAccount(0, fake_email_sender, transfer_fee)

    # Act (When)
    bank_account_sender.transfer(500, bank_account_receiver)

    # Assert (Then)
    assert bank_account_sender.get_balance() == 490
    assert bank_account_receiver.get_balance() == 500
