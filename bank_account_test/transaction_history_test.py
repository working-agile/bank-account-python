import pytest
from unittest.mock import Mock
from bank_account import BankAccount, InsufficientBalanceException

def test_deposits_should_be_informed_to_transaction_history():
    # Arrange (Given)
    transaction_history_mock = Mock()
    fake_email_sender = Mock()
    bank_account = BankAccount(1000, fake_email_sender, transaction_history_mock)

    # Act (When)
    bank_account.deposit(200)

    # Assert (Then)
    transaction_history_mock.inform_transaction.assert_called_with('deposit', 200)

def test_withdrawals_should_be_informed_to_transaction_history():
    # Arrange (Given)
    transaction_history_mock = Mock()
    fake_email_sender = Mock()
    bank_account = BankAccount(1000, fake_email_sender, transaction_history_mock)

    # Act (When)
    bank_account.withdraw(200)

    # Assert (Then)
    transaction_history_mock.inform_transaction.assert_called_with('withdraw', 200)

def test_withdrawal_that_does_not_go_through_is_not_informed_to_transaction_history():
    # Arrange (Given)
    transaction_history_mock = Mock()
    fake_email_sender = Mock()
    bank_account = BankAccount(1000, fake_email_sender, transaction_history_mock)

    # Act (When)
    with pytest.raises(InsufficientBalanceException):
        bank_account.withdraw(1001)

    # Assert (Then)
    transaction_history_mock.inform_transaction.assert_not_called()

def test_successful_transfers_are_registered_in_transaction_history():
    # Arrange (Given)
    transaction_history_sender_mock = Mock()
    transaction_history_receiver_mock = Mock()
    fake_email_sender = Mock()
    bank_account_sender = BankAccount(1000, fake_email_sender, transaction_history_sender_mock)
    bank_account_receiver = BankAccount(1000, fake_email_sender, transaction_history_receiver_mock)

    # Act (When)
    bank_account_sender.transfer(300, bank_account_receiver)

    # Assert (Then)
    transaction_history_sender_mock.inform_transaction.assert_called_with('withdraw', 300)
    transaction_history_receiver_mock.inform_transaction.assert_called_with('deposit', 300)

def test_unsuccessful_transfers_are_not_registered_in_transaction_history():
    # Arrange (Given)
    transaction_history_sender_mock = Mock()
    transaction_history_receiver_mock = Mock()
    fake_email_sender = Mock()
    bank_account_sender = BankAccount(1000, fake_email_sender, transaction_history_sender_mock)
    bank_account_receiver = BankAccount(1000, fake_email_sender, transaction_history_receiver_mock)

    # Act (When)
    with pytest.raises(InsufficientBalanceException):
        bank_account_sender.transfer(1001, bank_account_receiver)

    # Assert (Then)
    transaction_history_sender_mock.inform_transaction.assert_not_called()
    transaction_history_receiver_mock.inform_transaction.assert_not_called()