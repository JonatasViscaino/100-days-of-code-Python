# Day 53 - Data Entry Job Automation

This Python script performs web scraping on the Zillow Clone website, extracting property addresses, prices, and links. The scraped data is then submitted to a Google Form.

## Overview

- **Web Scraping Library:** BeautifulSoup, Selenium
- **Target Website:** [Zillow Clone](https://appbrewery.github.io/Zillow-Clone/)
- **Google Form Link:** [Submission Form](https://forms.gle/9JbJcsFs8if9p2a88)

## How it Works

1. **Web Scraping:**
   - Utilizes `requests` to get the HTML content of the Zillow Clone website.
   - BeautifulSoup is used to parse the HTML and extract property addresses, prices, and links.

2. **Chrome Driver Setup:**
   - Configures Chrome options and creates a Chrome WebDriver instance.

3. **Submitting Data to Google Form:**
   - A loop iterates through the extracted data.
   - For each iteration, the script opens the Google Form, inputs the address, price, and link using Selenium.
   - After filling in the form, a submission button is clicked, followed by a brief delay to ensure successful submission.

## Result

The final result of the web scraping can be found in the [Google Sheets document](https://docs.google.com/spreadsheets/d/1gOdlypG13uiD35xE32WuwNQXfXVgdn224N-36Q3-A7o/edit?usp=sharing).

Feel free to customize the script based on your requirements.
