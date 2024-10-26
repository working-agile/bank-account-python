import pytest
from unittest.mock import Mock
from bank_account import BankAccount

def test_how_a_bank_statement_with_empty_transaction_history_looks_like():
    # Arrange (Given)
    emailSenderMock = Mock()
    transaction_history_stub = Mock()
    empty_transaction_list = []
    transaction_history_stub.get_transaction_history.return_value = empty_transaction_list

    bank_account = BankAccount(1000, emailSenderMock, transaction_history_stub)

    # Act (When)
    bank_statement = bank_account.get_bank_statement()

    # Assert (Then)
    assert bank_statement == "balance:1000,transactionHistory:empty"

def test_how_a_bank_statement_with_one_deposit_looks_like():
    # Arrange (Given)
    emailSenderMock = Mock()
    transaction_history_stub = Mock()
    transaction_list = [50]
    transaction_history_stub.get_transaction_history.return_value = transaction_list

    bank_account = BankAccount(1000, emailSenderMock, transaction_history_stub)

    # Act (When)
    bank_statement = bank_account.get_bank_statement()

    # Assert (Then)
    assert bank_statement == "balance:1000,transactionHistory:[deposit:50]"

def test_how_a_bank_statement_with_one_deposit_and_a_withdrawal_looks_like():
    # Arrange (Given)
    emailSenderMock = Mock()
    transaction_history_stub = Mock()
    transaction_list = [50, -30]
    transaction_history_stub.get_transaction_history.return_value = transaction_list

    bank_account = BankAccount(1000, emailSenderMock, transaction_history_stub)

    # Act (When)
    bank_statement = bank_account.get_bank_statement()

    # Assert (Then)
    assert bank_statement == "balance:1000,transactionHistory:[deposit:50,withdrawal:30]"

def test_how_a_complete_bank_statement_should_look_like():
    # Arrange (Given)
    emailSenderMock = Mock()
    transaction_history_stub = Mock()
    transaction_list = [50, -30, -10, 550]
    transaction_history_stub.get_transaction_history.return_value = transaction_list

    bank_account = BankAccount(1000, emailSenderMock, transaction_history_stub)

    # Act (When)
    bank_statement = bank_account.get_bank_statement()

    # Assert (Then)
    assert bank_statement == "balance:1000,transactionHistory:[deposit:50,withdrawal:30,withdrawal:10,deposit:550]"
    