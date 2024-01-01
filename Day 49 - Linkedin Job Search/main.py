from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

# Constants
URL = "https://www.linkedin.com"
EMAIL = "YOUR_EMAIL"
PASSWORD = "YOUR_PASSWORD"
JOB = "Python Developer"

# Create and configure chrome driver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

# Opening URL
driver.get(URL)

# Log-in in LinkedIn
username = driver.find_element(By.NAME, value="session_key")
username.send_keys(EMAIL)
password = driver.find_element(By.NAME, value="session_password")
password.send_keys(PASSWORD)
button = driver.find_element(By.CSS_SELECTOR, value="div button.sign-in-form__submit-btn--full-width")
button.send_keys(Keys.ENTER)

input("Press Enter when you have solved the Captcha")

# Type Job in Search at LinkedIn
time.sleep(2)
search = driver.find_element(By.CLASS_NAME, value="search-global-typeahead__input")
search.send_keys(JOB, Keys.ENTER)

# Select only Jobs Options at LinkedIn
time.sleep(5)
buttons = driver.find_elements(By.CSS_SELECTOR, value='div.search-reusables__filters-bar-grouping ul li button')
for button in buttons:
    if button.text == "Jobs":
        button.click()

# Getting all jobs from the page with javascript
time.sleep(2)
for _ in range(5):
    driver.execute_script("document.querySelector('.jobs-search-results-list').scrollBy(0,1000)")
    time.sleep(3)
driver.execute_script("document.querySelector('.jobs-search-results-list').scrollBy(0,0)")


# Getting all the job listings and saving jobs
time.sleep(2)
all_listings = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container--clickable a")

for job in all_listings:
    time.sleep(2)
    print("Opening Job...")
    print(job.text)
    job.click()
    time.sleep(5)
    try:
        save_button = driver.find_element(By.CLASS_NAME, value="jobs-save-button")
        save_button.click()
    except NoSuchElementException:
        print("No save button, skipped.")
        continue



