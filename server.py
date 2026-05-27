from datetime import date

import pandas as pd

from backend import db_helper
from fastapi import FastAPI, HTTPException
from typing import List
from pydantic import BaseModel
app = FastAPI()
class SummaryExpense(BaseModel):
    amount:float
    category:str

class Expense(BaseModel):
    amount:float
    category:str
    notes:str
class DateRange(BaseModel):
    start_date:date
    end_date:date

@app.get("/expenses/{expense_date}", response_model=List[Expense])
def get_expenses(expense_date: date):
    expenses=db_helper.fetch_expenses_from_date(expense_date)
    return expenses
@app.post("/expenses/{expense_date}", response_model=List[Expense])
def create_expense(expense_date: date,expenses:List[Expense]):
    db_helper.delete_expenses(expense_date)
    for expense in expenses:
        db_helper.insert_expenses(expense_date,expense.amount,expense.category,expense.notes)
    return expenses
@app.post("/analytics_by_summary")
def analytics_summary(date_range:DateRange):

    expenses=db_helper.fetch_expense_summary(date_range.start_date,date_range.end_date)
    if expenses is None:
        raise HTTPException(status_code=500, detail="Couldn't analyse for the given dates")
    total=sum([expense['total'] for expense in expenses])
    break_down = {}
    for category_expense in expenses:
        percentage=((category_expense['total'] / total) * 100 if total!=0 else 0)
        break_down[category_expense['category']]={"total":category_expense['total'],"percentage":percentage}
    return break_down
@app.post("/analytics_by_month")
def analytics_month():
    expenses=db_helper. fetch_expense_monthly("2024-08-03","2024-09-30")
    df=pd.DataFrame(expenses)
    df["date"] = pd.to_datetime(df["expense_date"])
    df["month"] = df["month"] = df["date"].dt.strftime("%B")
    monthly_expense = (
        df.groupby("month")["total"]
        .sum()
        .reset_index()
    )
    return monthly_expense.to_dict("records")


