from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Models
class Transaction(BaseModel):
    id: int
    amount: float
    category: str
    description: Optional[str] = None

class Category(BaseModel):
    name: str

class BudgetAlert(BaseModel):
    threshold: float

# Sample data
transactions = []  # List to hold transactions
categories = []  # List to hold categories

@app.post("/transactions/", response_model=Transaction)
def create_transaction(transaction: Transaction):
    transactions.append(transaction)
    return transaction

@app.get("/transactions/", response_model=List[Transaction])
def get_transactions():
    return transactions

@app.post("/categories/", response_model=Category)
def create_category(category: Category):
    categories.append(category)
    return category

@app.get("/categories/", response_model=List[Category])
def get_categories():
    return categories

@app.get("/analytics/")
def get_analytics():
    total_expense = sum(transaction.amount for transaction in transactions)
    return {"total_expense": total_expense}

@app.post("/budget_alerts/", response_model=BudgetAlert)
def set_budget_alert(alert: BudgetAlert):
    return alert

@app.get("/export/csv/")
def export_to_csv():
    import pandas as pd
    df = pd.DataFrame(transactions)
    csv_file_path = "expenses.csv"
    df.to_csv(csv_file_path, index=False)
    return {"message": "CSV exported successfully!", "file_path": csv_file_path}