from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
from time import sleep

# Constants
EMAIL = 'YOUR_EMAIL'
PASSWORD = 'YOUR_PASSWORD'
URL = "https://www.instagram.com/"
# Add an account to check followers, example below is cristiano
SIMILAR_ACCOUNT = "cristiano"


class InstaFollower:

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        self.driver.get(URL)
        sleep(5)
        # Decline cookies
        cookiesdecline = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Decline optional cookies')]")
        cookiesdecline.click()
        sleep(3)
        # Add login and password credentials
        email = self.driver.find_element(By.NAME, "username")
        email.send_keys(EMAIL)
        password = self.driver.find_element(By.NAME, "password")
        password.send_keys(PASSWORD)
        sleep(2)
        password.send_keys(Keys.ENTER)
        sleep(5)
        # Recuse to accept to save login info information
        savelogininfobutton = self.driver.find_element(By.XPATH, value="//div[contains(text(),'Not now')]")
        if savelogininfobutton:
            savelogininfobutton.click()
        sleep(5)
        # Click on deny notifications button
        denynotifications = self.driver.find_element(By.XPATH, value="//button[contains(text(), 'Not Now')]")
        if denynotifications:
            denynotifications.click()

    def find_followers(self):
        sleep(5)
        # Open account and check followers
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/followers/")
        sleep(5)
        # Find pop-up window of followers and scroll down
        modal = self.driver.find_element(By.CLASS_NAME, value="_aano")
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            sleep(2)

    def follow(self):
        # Locate all "Follow" buttons.
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, value="button._ap30")
        print(all_buttons)
        # Clicking follow button and handle exceptions
        for button in all_buttons:
            try:
                print(button.text)
                if button.text == "Follow":
                    button.click()
                    sleep(1)
            # If error when clicking:
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Cancel')]")
                cancel_button.click()


# Bot Creation and Actions
bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
