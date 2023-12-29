from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

URL = "https://en.wikipedia.org/wiki/Main_Page"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

# Find an anchor tag with CSS
# n_articles = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# n_articles.click()

# Find element by Link Text
# all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# all_portals.click()

# Find search bar by Name
search = driver.find_element(By.NAME, value="search")
search.send_keys("Python", Keys.ENTER)
