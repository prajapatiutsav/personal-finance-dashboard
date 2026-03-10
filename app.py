from flask import Flask, render_template, jsonify, request, redirect
from analytics import *

app = Flask(__name__)


@app.route("/")
def home():

    df = load_data()

    total = total_expense(df)
    avg = average_expense(df)
    category = category_expense(df)
    prediction = predict_expense(df)
    transactions = recent_transactions(df)

    return render_template(
        "index.html",
        total=total,
        avg=avg,
        prediction=prediction,
        transactions=transactions
    )


@app.route("/data")
def data():

    df = load_data()

    category = category_expense(df)

    return jsonify(category)


@app.route("/add", methods=["POST"])
def add():

    date = request.form["date"]
    category = request.form["category"]
    amount = request.form["amount"]

    add_expense(date, category, amount)

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)