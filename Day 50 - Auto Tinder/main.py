from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Constants
URL = "https://www.tinder.com"
EMAIL = "YOUR_FACEBOOK_EMAIL"
PASSWORD = "YOUR_FACEBOOK_PASSWORD"

# Create and configure chrome driver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

# Opening URL
driver.get(URL)

# Log in with Facebook
time.sleep(5)
cookiesAccept = driver.find_element(By.XPATH, value='/html/body/div[1]/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]')
cookiesAccept.click()
logInButton = driver.find_element(By.XPATH, value='/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
logInButton.click()
time.sleep(3)
facebookButton = driver.find_element(By.XPATH, value='/html/body/div[2]/main/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button')
facebookButton.click()

window_tinder = driver.window_handles[0]
window_facebook = driver.window_handles[1]
driver.switch_to.window(window_facebook)

time.sleep(5)
loginFacebook = driver.find_element(By.XPATH, value='//*[@id="email"]')
loginFacebook.send_keys(EMAIL)
passwordFacebook = driver.find_element(By.XPATH, value='//*[@id="pass"]')
passwordFacebook.send_keys(PASSWORD, Keys.ENTER)

# Allow Location and Notifications in Tinder
driver.switch_to.window(window_tinder)
print(driver.title)
time.sleep(10)
allowButton = driver.find_element(By.XPATH, value='/html/body/div[2]/main/div/div/div/div[3]/button[1]/div[2]/div[2]').click()
time.sleep(5)
notificationButton = driver.find_element(By.XPATH, value='/html/body/div[2]/main/div/div/div/div[3]/button[1]/div[2]/div[2]').click()
time.sleep(5)

# Perform 100 likes
actions = ActionChains(driver)
for n in range(100):
    time.sleep(3)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.perform()
    print("It's a like.")