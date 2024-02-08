import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Constants
URL = "https://appbrewery.github.io/Zillow-Clone/"
FORMS_LINK = "https://forms.gle/9JbJcsFs8if9p2a88"

# Getting HTML data and creating soup
response = requests.get(URL)
data = response.text
soup = BeautifulSoup(data, "html.parser")

# Creating list of datas
addresses = [address.getText().strip().replace("|", "").replace("  ", " ") for address in soup.find_all("address")]
prices = [price.getText().strip()[0:6].split("+")[0] for price in soup.find_all(attrs={"data-test": "property-card-price"})]
links = [link.get("href") for link in soup.find_all("a", class_="property-card-link")]

# Create and configure chrome driver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

# Opening URL
for i in range(len(addresses)):
    driver.get(FORMS_LINK)
    time.sleep(1)
    input_address = driver.find_element(By.XPATH, value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
    input_address.send_keys(f"{addresses[i]}")
    input_price = driver.find_element(By.XPATH, value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
    input_price.send_keys(f"{prices[i]}")
    input_link = driver.find_element(By.XPATH, value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
    input_link.send_keys(f"{links[i]}")
    send_button = driver.find_element(By.XPATH, value="/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span")
    send_button.click()
    time.sleep(2)