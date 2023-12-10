# Day 36 - Stock News Alert Project

## Overview
This project is a simple yet effective Stock News Alert system that allows users to track and receive timely updates on the stock of their choice. The user can specify a stock symbol, and the system will send an email alert when the stock's variance exceeds 2% based on the latest available data. In addition to stock information, the email includes relevant news articles about the associated company.

## How It Works
The system utilizes two external APIs - Alpha Vantage for retrieving daily stock data and News API for fetching recent news related to the specified company. The user-configurable parameters such as stock symbol, company name, email credentials, and API keys are set as constants.

To determine the stock variance, the system compares the closing prices of the latest two available days, calculating the percentage change. If the variance is greater than or equal to 2%, an email alert is triggered.

The email notification includes an emoji indicating whether the stock is trending upward or downward, the percentage change, and the top three recent news articles related to the company.

## Configuration
Make sure to fill in the constants at the beginning of the script with your own values, including your stock API key, news API key, email credentials, and the stock symbol you want to track.

## Dependencies
This project uses the requests library for making API calls and the smtplib library for sending emails. Ensure these libraries are installed before running the script.

Feel free to customize and enhance the script to suit your preferences or integrate additional features. Happy tracking!