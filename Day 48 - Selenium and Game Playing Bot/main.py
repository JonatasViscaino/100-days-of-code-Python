from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://www.python.org/"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)
event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
event_titles = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")

events = {}

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "event": event_titles[n].text,
    }

print(events)

driver.quit()
