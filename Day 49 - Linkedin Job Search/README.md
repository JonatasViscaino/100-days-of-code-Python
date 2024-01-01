# Day 49 - LinkedIn Job Search

## Description
This Python script utilizes the Selenium library to automate job searching and saving on LinkedIn. The code performs the following tasks:

1. **Constants:**
- Defines constants such as the LinkedIn URL, email, and password.

2. **Chrome Driver Setup:**
- Configures a Chrome WebDriver with experimental options, allowing the browser to run in the background.

3. **Login to LinkedIn:**
- Navigates to LinkedIn, inputs the user's email and password, and logs into the platform.

4. **Handling Captcha:**
- Pauses the script and prompts the user to manually solve the Captcha.

5. **Job Search:**
- Searches for "Python Developer" jobs on LinkedIn using the search bar.

6. **Filtering Job Options:**
- Filters the search results to display only job listings.

7. **Scrolling through Job Listings:**
- Scrolls through the job listings using JavaScript to dynamically load more results.

8. **Saving Job Listings:**
- Opens each job listing, prints its details, and attempts to save it. If no "Save" button is found, the script skips to the next job.

Please note that the script may require adjustments based on changes to the LinkedIn website structure or terms of service, and it should be used responsibly in compliance with LinkedIn's policies.