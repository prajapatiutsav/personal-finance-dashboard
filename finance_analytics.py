import pandas as pd
import numpy as np
import json
from datetime import datetime


def load_data():

    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except:
        data = []

    df = pd.DataFrame(data)

    if not df.empty:
        df["date"] = pd.to_datetime(df["date"])

    return df


def save_data(data):

    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)


def add_expense(date, category, amount):

    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except:
        data = []

    data.append({
        "date": date,
        "category": category,
        "amount": float(amount)
    })

    save_data(data)


def monthly_expense(df):

    if df.empty or "amount" not in df.columns:
        return 0

    current_month = datetime.now().month
    current_year = datetime.now().year

    monthly_data = df[
        (df["date"].dt.month == current_month) &
        (df["date"].dt.year == current_year)
    ]

    return float(monthly_data["amount"].sum())


def weekly_expense(df):

    if df.empty or "amount" not in df.columns:
        return 0

    current_week = datetime.now().isocalendar()[1]
    current_year = datetime.now().year

    weekly_data = df[
        (df["date"].dt.isocalendar().week == current_week) &
        (df["date"].dt.year == current_year)
    ]

    return float(weekly_data["amount"].sum())


def average_expense(df):

    if df.empty or "amount" not in df.columns:
        return 0

    return float(df["amount"].mean())


def category_expense(df):

    if df.empty or "amount" not in df.columns:
        return {}

    return df.groupby("category")["amount"].sum().to_dict()


def recent_transactions(df):

    if df.empty:
        return []

    return df.tail(5).to_dict(orient="records")


def predict_expense(df):

    if df.empty or "amount" not in df.columns:
        return 0

    expenses = df["amount"].values

    if len(expenses) < 2:
        return float(expenses[0]) if len(expenses) == 1 else 0

    days = np.arange(len(expenses))

    slope, intercept = np.polyfit(days, expenses, 1)

    next_day = len(expenses)

    prediction = slope * next_day + intercept

    return round(float(prediction), 2)
