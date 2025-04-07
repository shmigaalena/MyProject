class Expense:
    def __init__(self, amount, category):
        if amount < 0:
            raise ValueError("Amount must be non-negative")
        self.amount = amount
        self.category = category

    def __repr__(self):
        return f"<{self.category}: {self.amount}>"


class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, amount, category):
        expense = Expense(amount, category)
        self.expenses.append(expense)

    def total_expense(self):
        return sum(e.amount for e in self.expenses)

    def expense_by_category(self, category):
        return sum(e.amount for e in self.expenses if e.category == category)

    def clear_expenses(self):
        self.expenses = []

    def get_expenses(self):
        return self.expenses.copy()
