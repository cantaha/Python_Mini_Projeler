from selenium import webdriver
import time
from selenium.webdriver.common.by import By

class GitHub:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Safari()
        self.followers = []

    def login(self):
        self.driver.get("https://github.com/login")
        time.sleep(2)
        self.driver.maximize_window()
        time.sleep(2)

        self.driver.find_element(By.XPATH, "//*[@id='login_field']").send_keys(self.username)
        self.driver.find_element(By.XPATH, "//*[@id='password']").send_keys(self.password)
        time.sleep(2)

        self.driver.find_element(By.XPATH, "//*[@id='login']/div[4]/form/div/input[13]").click() #".click" tuşa basma komutu
        time.sleep(5)

    def loadFollowers(self):
        items = self.driver.find_elements(By.CSS_SELECTOR, ".d-table.table-fixed")
        for item in items:
            self.followers.append(item.find_element(By.CSS_SELECTOR, ".f4.Link--primary").text)

    def getFollowers(self):
        self.driver.get("https://github.com/sadikturan?tab=followers") # burada "sadıkturan" kullanıcı adını kullandım çünkü benim hiç followers'm yok amk. üzüldüm. adamın 5k civarı kod çok uzun çalışmak zorunda kalıyor.
        time.sleep(2)
        self.loadFollowers()

        while True:
            pages = self.driver.find_element(By.CLASS_NAME, "pagination").find_elements(By.TAG_NAME, "a")
            if len(pages) == 1:
                if pages[0].text == "Next":
                    pages[0].click()
                    time.sleep(2)
                    self.loadFollowers()

                else:
                    break
            else:
                for page in pages:
                    if page.text == "Next":
                        page.click()
                        time.sleep(2)
                    else:
                        continue



username = "cantaha"
password = "*************"
github = GitHub(username, password)
github.login()
github.getFollowers()
print(github.followers)