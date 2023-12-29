from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def check_products():
    items = driver.find_elements(By.CSS_SELECTOR, value="div.product.unlocked")
    try:
        for n in range(len(items), -1, -1):
            product = driver.find_element(By.ID, value=f"product{n}")
            product_price = driver.find_element(By.ID, value=f"productPrice{n}")
            number_of_cookies = driver.find_element(By.ID, value="cookies")
            if int(product_price.text.replace(",", "")) < int(number_of_cookies.text.split()[0].replace(",", "")):
                product.click()
    finally:
        pass


URL = "https://orteil.dashnet.org/cookieclicker/"

# Create and configure chrome driver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

# Opening URL
driver.get(URL)

# Selecting language
time.sleep(3)
language = driver.find_element(By.CSS_SELECTOR, "#langSelect-EN")
language.click()

# Clicking on cookie
cookie = driver.find_element(By.ID, value="bigCookie")

# Timers
timeout = time.time() + 5
stop = time.time() + 5 * 60

while time.time() < stop:
    cookie.click()
    if time.time() > timeout:
        check_products()
        timeout = time.time() + 5

if time.time() > stop:
    cookies_per_second = driver.find_element(By.ID, value="cookies").text
    print(cookies_per_second)
