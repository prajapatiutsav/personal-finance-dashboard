from flask import Flask, render_template, jsonify, request, redirect
import finance_analytics as analytics

app = Flask(__name__)


@app.route("/")
def home():

    df = analytics.load_data()

    month_total = analytics.monthly_expense(df)
    week_total = analytics.weekly_expense(df)
    avg = analytics.average_expense(df)
    prediction = analytics.predict_expense(df)
    transactions = analytics.recent_transactions(df)

    return render_template(
        "index.html",
        month_total=month_total,
        week_total=week_total,
        avg=avg,
        prediction=prediction,
        transactions=transactions
    )


@app.route("/data")
def data():

    df = analytics.load_data()

    category = analytics.category_expense(df)

    return jsonify(category)


@app.route("/add", methods=["POST"])
def add():

    date = request.form["date"]
    category = request.form["category"]
    amount = request.form["amount"]

    analytics.add_expense(date, category, amount)

    return redirect("/")


@app.route("/clear", methods=["POST"])
def clear_data():

    import json

    with open("data.json", "w") as file:
        json.dump([], file)

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
