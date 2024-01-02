from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Constants
PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = "jonatasvrodriguez@gmail.com"
TWITTER_PASSWORD = "Jonatas123"
TWITTER_USERNAME = "JojoViscaino"


class InternetSpeedTwitterBot:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        button_go = self.driver.find_element(By.CLASS_NAME, "js-start-test")
        button_go.click()
        time.sleep(60)
        self.down = self.driver.find_element(By.CLASS_NAME, value="download-speed").text
        self.up = self.driver.find_element(By.CLASS_NAME, value="upload-speed").text
        print(f"down: {self.down}")
        print(f"up: {self.up}")

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/i/flow/login")
        time.sleep(5)
        email = self.driver.find_element(By.NAME, "text")
        email.send_keys(TWITTER_EMAIL, Keys.ENTER)
        time.sleep(5)
        username = self.driver.find_element(By.TAG_NAME, "input")
        username.send_keys(TWITTER_USERNAME, Keys.ENTER)
        time.sleep(5)
        password = self.driver.find_element(By.NAME, "password")
        password.send_keys(TWITTER_PASSWORD, Keys.ENTER)
        time.sleep(5)
        draft = self.driver.find_element(By.CLASS_NAME, value="public-DraftStyleDefault-block")
        draft.send_keys(f"Hey Internet Provider, why is my internet speed {self.down} down"
                        f"/{self.up} up when I paid for 150 down/10 up?")
        button_post = self.driver.find_element(By.XPATH,
                                               value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div['
                                                     '1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div['
                                                     '2]/div/div/div/div[3]/div/span/span')
        button_post.click()


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
