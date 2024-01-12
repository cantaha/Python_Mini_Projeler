import time

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Safari()
url = "https://www.themoviedb.org/"
driver.get(url)
searchInput = driver.find_element(By.XPATH, '//*[@id="inner_search_v4"]')
searchInput.send_keys("walking")
driver.maximize_window()
time.sleep(2)
searchInput.send_keys(Keys.ENTER)
time.sleep(3)
driver.close()

