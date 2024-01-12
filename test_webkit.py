#selenium

from selenium import webdriver
import time

driver = webdriver.Safari()
url = "http://github.com"
driver.get(url)

time.sleep(2)
driver.maximize_window()
time.sleep(2)
driver.save_screenshot("github.com-homepagescreenshot.png")

url = "http://github.com/cantaha/githubdeneme"
driver.get(url)
print(driver.title)
if "githubdeneme" in driver.title:
    driver.save_screenshot("github-cantaharepos.png")

time.sleep(2)
driver.back()
time.sleep(2)
driver.close()