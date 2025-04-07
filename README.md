# Expense Tracker

A simple Python project for tracking personal expenses via code. It supports adding expenses with categories, calculating total spending, filtering by category, clearing history, and counting expenses. This project is designed to demonstrate good practices in modular Python design, unit testing, and CI/CD with GitHub Actions.

## Features

- Add expenses with amount and category
- Calculate total expense
- Calculate expense by category
- Clear all expenses
- Count number of expense entries

## Project Structure

```
/project_root
├── .github/workflows/ci.yml        # GitHub Actions CI/CD pipeline
├── src/
│   └── main.py                     # Core logic: Expense and ExpenseTracker classes
├── tests/
│   └── test_main.py                # Unit tests written with pytest
├── requirements.txt                # Python dependencies
├── sonar-project.properties        # SonarQube configuration
├── setup.py                        # Project setup for coverage and linting
├── README.md                       # Project documentation
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/ExpenseTracker.git
cd ExpenseTracker
```

2. Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

3. Install the dependencies:

```bash
pip install -r requirements.txt
```

## Usage

This project is written as a library-style module and does not include a CLI or UI (yet). Use the `ExpenseTracker` class in your own Python scripts or notebooks:

```python
from src.main import ExpenseTracker

tracker = ExpenseTracker()
tracker.add_expense(50, "food")
tracker.add_expense(30, "transport")

print(tracker.total_expense())               # 80
print(tracker.expense_by_category("food"))   # 50
print(tracker.count_expenses())              # 2
```

## Running Tests

To run the unit tests and generate a coverage report:

```bash
coverage run -m pytest
coverage report
```

## CI/CD

GitHub Actions workflow (`.github/workflows/ci.yml`) automatically performs the following checks:

- Run unit tests and check test coverage
- Enforce code style with flake8 and black via Reviewdog
- Count lines of code using `cloc`
- Analyze code quality with SonarQube
- Ensure code review approval before merge

## SonarQube Integration

SonarQube analysis is configured using the `sonar-project.properties` file. It includes paths to source code, tests, and coverage reports. The analysis runs automatically as part of the `sonarqube` job in the CI pipeline.

## Example Output (Python interactive)

```python
>>> tracker = ExpenseTracker()
>>> tracker.add_expense(100, "books")
>>> tracker.add_expense(50, "food")
>>> tracker.total_expense()
150
>>> tracker.expense_by_category("books")
100
>>> tracker.count_expenses()
2
```
