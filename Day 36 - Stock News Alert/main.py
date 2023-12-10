import requests
from datetime import datetime, timedelta
import smtplib
from email.message import EmailMessage

# Constants
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API = "XXXXX"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API = "XXXXX"
MY_EMAIL = "XXXXX@gmail.com"
GMAIL_PASS = "XXXXXXXXXXXXXXXXXX"

# Date Values
# For Sunday, it will select the latest stocks of Thursday and Friday
if datetime.now().weekday() == 6:
    yesterday_date = datetime.strftime(datetime.now() - timedelta(2), '%Y-%m-%d')
    bef_yesterday_date = datetime.strftime(datetime.now() - timedelta(3), '%Y-%m-%d')
# For Monday, it will select the latest stock of Thursday and Friday
elif datetime.now().weekday() == 0:
    yesterday_date = datetime.strftime(datetime.now() - timedelta(3), '%Y-%m-%d')
    bef_yesterday_date = datetime.strftime(datetime.now() - timedelta(4), '%Y-%m-%d')
# For Tuesday, it will select the latest stock of Thursday and Friday
elif datetime.now().weekday() == 1:
    yesterday_date = datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d')
    bef_yesterday_date = datetime.strftime(datetime.now() - timedelta(4), '%Y-%m-%d')
else:
    yesterday_date = datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d')
    bef_yesterday_date = datetime.strftime(datetime.now() - timedelta(2), '%Y-%m-%d')

# Getting data from STOCK API:
stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API,
}

response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]

yest_close_price = float(data[yesterday_date]["4. close"])
bef_yest_close_price = float(data[bef_yesterday_date]["4. close"])
diff = yest_close_price - bef_yest_close_price
diff_percent = round((diff/yest_close_price)*100, 2)

# Creating Emoji for E-mail
if diff > 0:
    up_down = "📈"
else:
    up_down = "📉"

# Getting data from NEWS API:
news_parameters = {
    "q": COMPANY_NAME,
    "searchIn": "title",
    "apikey": NEWS_API
}

response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
response.raise_for_status()
articles = response.json()['articles']

email_body_list = []
for article in articles[:3]:
    headline = article["title"]
    description = article["description"]
    url = article["url"]
    date = datetime.fromisoformat(article["publishedAt"]).strftime('%d-%m-%Y')
    body_string = (f"\nHEADLINE: {headline}\nPUBLISHED DATE: {date}\n"
                   f"DESCRIPTION: {article['description']}\nURL: {article['url']}\n")
    email_body_list.append(body_string)

if abs(diff_percent) >= 2:
    subject = f"{COMPANY_NAME}: {STOCK} {up_down} {diff_percent}%"
    body = '\n'.join(email_body_list)
    message = EmailMessage()
    message.add_header("From", MY_EMAIL)
    message.add_header("To", MY_EMAIL)
    message.add_header("Subject", subject)
    message.set_payload(body, "utf-8")
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=GMAIL_PASS)
        connection.send_message(message, to_addrs=MY_EMAIL, from_addr=MY_EMAIL)
