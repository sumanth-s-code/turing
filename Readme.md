# Budget Tracker CLI Tool

## Overview

Budget Tracker is a modular command-line interface (CLI) tool for tracking your income and expenses. It uses a local SQLite database to store transactions and provides summary reports.

## Features

- **Add Transactions:** Record income or expense transactions.
- **List Transactions:** View all transactions in a formatted table.
- **Summary Report:** Display total income, total expenses, and net balance.
- **Delete Transactions:** Remove a transaction by specifying its ID.

## Project Structure

budget-tracker/
├── budget_tracker/
│   ├── __init__.py
│   ├── db.py         # Database operations and business logic.
│   └── cli.py        # CLI argument parsing and main entry point.
├── tests/
│   └── test_budget_tracker.py  # Unit tests for database operations.
├── requirements.txt  # External dependencies.
├── README.md         # Project documentation.
└── Dockerfile        # Containerization instructions.


## Installation

1. **Clone the repository:**

   ```bash
   git clone https://https://github.com/sumanth-s-code/turing.git
   cd budget-tracker

2. **Create and activate a virtual environment (optional but recommended):**
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

3. **Install Dependencies**
pip install -r requirements.txt

