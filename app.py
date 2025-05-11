from flask import Flask, render_template, request
from services.coingecko import get_multiple_prices, get_price_history

app = Flask(__name__)

COINS = {
    "bitcoin": "Bitcoin",
    "ethereum": "Ethereum",
    "dogecoin": "Dogecoin",
    "solana": "Solana",
    "cardano": "Cardano",
}


@app.route("/", methods=["GET", "POST"])
def index():
    selected_coin = "bitcoin"
    days = "7"
    if request.method == "POST":
        selected_coin = request.form.get("coin", "bitcoin").lower()
        days = request.form.get("days", "7")

    prices = get_multiple_prices(COINS.keys())
    chart_data = get_price_history(selected_coin, days)

    return render_template(
        "index.html",
        coins=COINS,
        prices=prices,
        selected_coin=selected_coin,
        chart_data=chart_data,
        days=days,
    )


if __name__ == "__main__":
    app.run(debug=True)
