from bs4 import BeautifulSoup
import requests
import smtplib

# Product URL and constants
AMAZON_URL = ("https://www.amazon.de/-/en/kindle-paperwhite-16-gb-now-with-a-68-display-and-adjustable-warm-light"
              "-with-ads/dp/B09TMP5Y2S/")
MY_EMAIL = "YOUR_EMAIL"
PASSWORD = "YOUR_PASS"

# get header from https://myhttpheader.com/
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,pt;q=0.8",
}

# Retrieving price from Amazon Website
data = requests.get(url=AMAZON_URL, headers=header)
soup = BeautifulSoup(data.text, "html.parser")
price = soup.select_one(".a-offscreen").text.split("€")[1]
product_name = soup.select_one("#productTitle").getText().strip()

# Decide what your price range would be to send an e-mail
if float(price) < 115:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Offer Amazon Price!\n\n ALERT PRICE: {product_name} is now EUR {price}\n"
                f"Check it out at: {AMAZON_URL}"
        )
