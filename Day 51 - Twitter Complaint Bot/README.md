# Day 51 - Internet Speed Twitter Bot

## Description
This Python script automates internet speed testing using speedtest.net and notifies your internet service provider through Twitter if the speed falls below promised values.  
Selenium is employed for web automation, facilitating interaction with speedtest.net and Twitter.

## Dependencies:
- **Selenium:** Utilized for web automation to interact with speedtest.net and Twitter.

## Functionality:
- The **InternetSpeedTwitterBot** class initializes a Chrome WebDriver.
- The **get_internet_speed** method tests internet speed on speedtest.net and prints the results.
- The **tweet_at_provider** method logs into Twitter, creating a tweet mentioning the internet provider and indicating the speed discrepancy.

## Important:
- Ensure the Chrome WebDriver is installed with its path configured.
- Adjust sleep durations as needed based on internet speed test duration and Twitter response times.