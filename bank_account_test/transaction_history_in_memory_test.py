from bank_account import TransactionHistoryInMemory

def test_returns_the_transaction_history_without_transactions():
    # Arrange (Given)
    transaction_history = TransactionHistoryInMemory()

    # Act (When)
    transaction_list = transaction_history.get_transaction_history()

    # Assert (Then)
    assert transaction_list == []

def test_informing_a_single_deposit():
    # Arrange (Given)
    transaction_history = TransactionHistoryInMemory()

    # Act (When)
    transaction_history.inform_transaction('deposit', 50)

    # Assert (Then)
    transaction_list = transaction_history.get_transaction_history()
    assert transaction_list != []
    assert len(transaction_list) == 1
    assert transaction_list[0] == 50

def test_informing_a_single_withdrawal():
    # Arrange (Given)
    transaction_history = TransactionHistoryInMemory()

    # Act (When)
    transaction_history.inform_transaction('withdraw', 50)

    # Assert (Then)
    transaction_list = transaction_history.get_transaction_history()
    assert transaction_list != []
    assert len(transaction_list) == 1
    assert transaction_list[0] == -50

def test_informing_a_deposit_and_a_withdrawal():
    # Arrange (Given)
    transaction_history = TransactionHistoryInMemory()

    # Act (When)
    transaction_history.inform_transaction('deposit', 100)
    transaction_history.inform_transaction('withdraw', 50)

    # Assert (Then)
    transaction_list = transaction_history.get_transaction_history()
    assert transaction_list != []
    assert len(transaction_list) == 2
    assert transaction_list[0] == 100
    assert transaction_list[1] == -50

def test_the_transaction_history_does_not_expose_internal_objects():
    # Arrange (Given)
    transaction_history = TransactionHistoryInMemory()
    transaction_history.inform_transaction('deposit', 100)
    transaction_list = transaction_history.get_transaction_history()

    # Act (When)
    transaction_list[0] = 200

    # Assert (Then)
    transaction_list2 = transaction_history.get_transaction_history()
    assert transaction_list2[0] == 100