import sys
import os

import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.main import ExpenseTracker, Expense

def test_add_expense():
    tracker = ExpenseTracker()
    tracker.add_expense(50, "food")
    assert len(tracker.expenses) == 1
    assert tracker.expenses[0].amount == 50
    assert tracker.expenses[0].category == "food"


def test_total_expense():
    tracker = ExpenseTracker()
    tracker.add_expense(30, "food")
    tracker.add_expense(20, "transport")
    assert tracker.total_expense() == 50


def test_expense_by_category():
    tracker = ExpenseTracker()
    tracker.add_expense(100, "food")
    tracker.add_expense(30, "food")
    tracker.add_expense(70, "transport")
    assert tracker.expense_by_category("food") == 130
    assert tracker.expense_by_category("transport") == 70
    assert tracker.expense_by_category("entertainment") == 0


def test_clear_expenses():
    tracker = ExpenseTracker()
    tracker.add_expense(10, "misc")
    tracker.clear_expenses()
    assert tracker.expenses == []


def test_get_expenses_returns_copy():
    tracker = ExpenseTracker()
    tracker.add_expense(25, "books")
    returned = tracker.get_expenses()
    returned.append(Expense(100, "fake"))
    assert len(tracker.expenses) == 1  # має залишитись незмінним


def test_negative_amount_raises():
    tracker = ExpenseTracker()
    with pytest.raises(ValueError):
        tracker.add_expense(-50, "food")
