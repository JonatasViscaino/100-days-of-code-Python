import requests
from datetime import datetime, timedelta

# Constants
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API = "8PQY1VQG0RMTSYM0"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API = "42c6b37f816d4cfd8d82dea21c88b8f5"

# Date Values
yesterday_date = datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d')
bef_yesterday_date = datetime.strftime(datetime.now() - timedelta(2), '%Y-%m-%d')

# API Parameters
stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API,
}

news_parameters = {
    "q": COMPANY_NAME,
    "apikey": NEWS_API
}
## STEP 1: Use https://newsapi.org/docs/endpoints/everything


#response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
#response.raise_for_status()
#print(response.json())
#data = response.json()["Time Series (Daily)"]

#yest_close_price = float(data[yesterday_date]["4. close"])
#bef_yest_close_price = float(data[bef_yesterday_date]["4. close"])
#diff = yest_close_price - bef_yest_close_price
#print(yest_close_price)
#print(bef_yest_close_price)
#if (diff/yest_close_price)*100 > 5:
#    print("Get News")


## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME.
#HINT 1: Think about using the Python Slice Operator

response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
response.raise_for_status()

print(response.json()["articles"])

## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number.
#HINT 1: Consider using a List Comprehension.

