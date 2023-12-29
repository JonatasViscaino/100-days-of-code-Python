from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# URL to open website
URL = "http://secure-retreat-92358.herokuapp.com/"

# Create and configure chrome driver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

# Opening URL
driver.get(URL)

# Getting fields from the form
f_name = driver.find_element(By.NAME, value="fName")
l_name = driver.find_element(By.NAME, value="lName")
email = driver.find_element(By.NAME, value="email")

# Filling out the form and submitting
f_name.send_keys("Jonatas")
l_name.send_keys("Rodriguez")
email.send_keys("jonatas@gmail.com")

# Locating the button
button = driver.find_element(By.CSS_SELECTOR, value="form button")
button.click()

