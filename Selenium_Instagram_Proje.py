import time
from selenium import webdriver
from selenium.webdriver.common.by import By


username = "********" #kullanıcı adı ve şifre girilmeli
password = "********"
class SeleniumInstagramProje:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
        time.sleep(1)
        # self.driver.maximize_window()
        time.sleep(1)
        self.driver.find_element(By.NAME, "username").send_keys(self.username)
        self.driver.find_element(By.NAME, "password").send_keys(self.password)
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR, 'div[role="button"]').click()
        time.sleep(3)
        self.driver.find_element(By.CLASS_NAME, '_a9-z').find_element(By.CSS_SELECTOR,"._a9--._ap36._a9_1").click()
        time.sleep(3)


    def getFollowers(self):
        self.followers = []
        self.driver.get(f"https://www.instagram.com/{self.username}/followers/")
        time.sleep(4)
        dialog = self.driver.find_element(By.CSS_SELECTOR, 'div[role="dialog"]')
        followersCount = len(dialog.find_elements(By.CSS_SELECTOR, '.x1dm5mii.x16mil14.xiojian.x1yutycm.x1lliihq.x193iq5w.xh8yej3'))
        print(f"First Count: {followersCount}")
        # action = webdriver.ActionChains(self.driver)
        while True:
            popUp = self.driver.find_element(By.CSS_SELECTOR, "._aano")
            self.driver.execute_script(
                'arguments[0].scrollTop = arguments[0].scrollHeight;',
                popUp)
            time.sleep(2)
            newCount = len(dialog.find_elements(By.CSS_SELECTOR, '.x1dm5mii.x16mil14.xiojian.x1yutycm.x1lliihq.x193iq5w.xh8yej3'))
            if followersCount != newCount:
                followersCount = newCount
                print(f"Updated Count: {newCount}")
                time.sleep(2)
            else:
                break

        followers = dialog.find_elements(By.CSS_SELECTOR, '.x1dm5mii.x16mil14.xiojian.x1yutycm.x1lliihq.x193iq5w.xh8yej3')
        for i in followers:
            link = i.find_element(By.CSS_SELECTOR, '._ap3a._aaco._aacw._aacx._aad7._aade').text # html kodlarında aradığımı bulmakta zorlandım. tag'lerde hata olabilir. tekrar kontrol et.
            self.followers.append(link)

        print(self.followers)
        time.sleep(2)

insta = SeleniumInstagramProje(username, password)
insta.login()
insta.getFollowers()
