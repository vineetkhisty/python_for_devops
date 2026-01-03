import requests

API_KEY = "H3GDSCRN6XAQKYNR"

symbol = input("Enter the symbol you wish to get the stock report: e.g(IBM,AMZN,GOGL etc):")

# is_timeseries = input("Do you wish to view time series data? : (True,False) : ")



def get_stock_market_data(symbol):
    API_URL = "https://www.alphavantage.co/"
    query= f"query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}"
    response= requests.get(url=API_URL+query)

    for key,value in response.json().items():
        if key == "Meta Data":
            print(key,value)

get_stock_market_data(symbol)