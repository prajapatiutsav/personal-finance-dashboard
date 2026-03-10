import pandas as pd
import numpy as np
import json


def load_data():

    with open("data.json", "r") as file:
        data = json.load(file)

    df = pd.DataFrame(data)

    return df


def save_data(data):

    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)


def add_expense(date, category, amount):

    with open("data.json", "r") as file:
        data = json.load(file)

    data.append({
        "date": date,
        "category": category,
        "amount": float(amount)
    })

    save_data(data)


def total_expense(df):

    return float(df["amount"].sum())


def average_expense(df):

    return float(df["amount"].mean())


def category_expense(df):

    return df.groupby("category")["amount"].sum().to_dict()


def recent_transactions(df):

    return df.tail(5).to_dict(orient="records")


def predict_expense(df):

    expenses = df["amount"].values

    days = np.arange(len(expenses))

    slope, intercept = np.polyfit(days, expenses, 1)

    next_day = len(expenses)

    prediction = slope * next_day + intercept

    return round(float(prediction), 2)