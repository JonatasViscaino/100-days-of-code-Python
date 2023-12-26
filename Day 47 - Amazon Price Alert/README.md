# Day 47 - Amazon Price Alert

This Python script utilizes BeautifulSoup, Requests, and smtplib to track the price of a specific product on Amazon. The product being monitored is the Kindle Paperwhite. The script fetches the current price and product name from the Amazon product page and sends an email notification if the price drops below a specified threshold.

## Key Features:
Utilizes BeautifulSoup for web scraping Amazon's product page.
Sends email notifications using smtplib if the product price falls below a defined threshold.
Customizable: Users can set their Amazon product URL, email credentials, and price threshold.

## Usage:
1. Specify the Amazon product URL, email credentials, and desired price threshold.
2. Run the script periodically to track price changes.

This script is useful for individuals who want to be alerted when a specific product on Amazon becomes more affordable.