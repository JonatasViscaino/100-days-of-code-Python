import requests
from datetime import datetime, timedelta
import smtplib
from email.message import EmailMessage

# Constants
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API = "8PQY1VQG0RMTSYM0"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API = "42c6b37f816d4cfd8d82dea21c88b8f5"
MY_EMAIL = "jonatasmviscaino@gmail.com"
GMAIL_PASS = "XXXX"

# Date Values
yesterday_date = datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d')
bef_yesterday_date = datetime.strftime(datetime.now() - timedelta(2), '%Y-%m-%d')

# Getting data from STOCK API:
# stock_parameters = {
#     "function": "TIME_SERIES_DAILY",
#     "symbol": STOCK,
#     "apikey": STOCK_API,
# }
#
# response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
# response.raise_for_status()
# data = response.json()["Time Series (Daily)"]
#
# yest_close_price = float(data[yesterday_date]["4. close"])
# bef_yest_close_price = float(data[bef_yesterday_date]["4. close"])
# diff = yest_close_price - bef_yest_close_price
# diff_percent = round((diff/yest_close_price)*100)

# Creating Emoji for E-mail
up_down = "TEST"
# if diff > 0:
#     up_down = "UP"
# else:
#     up_down = "DOWN"

# Getting data from NEWS API:
news_parameters = {
    "q": COMPANY_NAME,
    "searchIn": "title",
    "apikey": NEWS_API
}

response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
response.raise_for_status()
articles = response.json()['articles']

email_body_list = [(f"{STOCK}\nHeadline: {article['title']}\n\n"
                    f"Description: {article['description']}\n\nUrl: {article['url']}") for article in articles[:3]]

#if abs(diff_percent) >= 0:
subject = f"{COMPANY_NAME}:{up_down} %"
body = '\n'.join(email_body_list)
message = EmailMessage()
message.add_header("From", MY_EMAIL)
message.add_header("To", MY_EMAIL)
message.add_header("Subject", subject)
message.set_payload(body, "utf-8")
with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=MY_EMAIL, password=GMAIL_PASS)
    connection.sendmail(msg=message, to_addrs=MY_EMAIL, from_addr=MY_EMAIL)
