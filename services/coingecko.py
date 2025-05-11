import requests


def get_multiple_prices(coin_ids, vs_currency="usd"):
    ids = ",".join(coin_ids)
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={ids}&vs_currencies={vs_currency}"
    response = requests.get(url)
    return response.json()


def get_price_history(coin_id, days=7):
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart?vs_currency=usd&days={days}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()["prices"]
    return []
