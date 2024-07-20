# Expense Tracker + Analytics API

This project is designed to provide a simple Expense Tracker and Analytics API using **FastAPI** and **SQLite**.

## Features
- Add, update, delete, and retrieve expenses.
- Basic analytics to summarize expenditures.

## Technologies Used
- FastAPI for building the API.
- SQLite as the database for storing expense data.

## Getting Started
To run the API, follow these steps:
1. Clone the repository:
   ```bash
   git clone https://github.com/nursultanbeishenbekov20008-cmyk/Expense-tracker-Analytics.git
   ```
2. Install the required packages:
   ```bash
   pip install fastapi[all] sqlite3
   ```
3. Run the API:
   ```bash
   uvicorn main:app --reload
   ```

## API Endpoints
- **`GET /expenses/`** - Retrieve all expenses.
- **`POST /expenses/`** - Add a new expense.
- **`PUT /expenses/{id}`** - Update an existing expense.
- **`DELETE /expenses/{id}`** - Delete an expense.

## License
MIT License. See LICENSE file for details.