import requests

API_URL = "https://api.restful-api.dev"

query = "/objects"

request_url = f"{API_URL}{query}"

def get_stock_prices():
    response= requests.get(url=request_url)

    print(response.json())


get_stock_prices()