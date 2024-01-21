import time
from selenium import webdriver
from selenium.webdriver.common.by import By


username = "********" #kullanıcı adı ve şifre girilmeli
password = "********"
class SeleniumInstagramProje:
    def __init__(self, username, password):
        self.driverProfile = webdriver.ChromeOptions()
        self.driverProfile.add_experimental_option("prefs", {"intl.accept_languages": "en,en_US"})
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(options=self.driverProfile)


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
        time.sleep(2)
        self.driver.find_element(By.CLASS_NAME, '_a9-z').find_element(By.CSS_SELECTOR,"._a9--._ap36._a9_1").click()
        time.sleep(2)


    def getFollowers(self, max):
        self.followers = []
        self.driver.get(f"https://www.instagram.com/{self.username}/followers/")
        time.sleep(4)
        dialog = self.driver.find_element(By.CSS_SELECTOR, 'div[role="dialog"]')
        followersCount = len(dialog.find_elements(By.CSS_SELECTOR, '.x1dm5mii.x16mil14.xiojian.x1yutycm.x1lliihq.x193iq5w.xh8yej3'))
        print(f"First Count: {followersCount}")

        while followersCount < max:
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
        usermax = 0
        for i in followers:
            link = i.find_element(By.CSS_SELECTOR, '._ap3a._aaco._aacw._aacx._aad7._aade').text # html kodlarında aradığımı bulmakta zorlandım. tag'lerde hata olabilir. tekrar kontrol et.
            self.followers.append(link)
            usermax += 1
            if usermax == max:
                break

        print(self.followers)
        time.sleep(2)

        with open("instausers.txt", "w", encoding="UTF-8") as instausers:
            for follower in self.followers:
                instausers.write(follower + "\n")

    def followUser(self, username):
        time.sleep(1)
        self.driver.get(f"https://www.instagram.com/{username}")
        time.sleep(4)
        followButton = self.driver.find_element(By.TAG_NAME, 'button')
        if followButton.text != "Following":
            followButton.click()
            time.sleep(3)
            print("Done!")
        else:
            print("Following user already")
            pass
        time.sleep(3)

    def unfollowUser(self, username):
        time.sleep(1)
        self.driver.get(f"https://www.instagram.com/{username}")
        time.sleep(4)
        unfollowButton = self.driver.find_element(By.TAG_NAME, "button")
        if unfollowButton.text == "Following":
            unfollowButton.click()
            time.sleep(4)
            self.driver.find_element(By.XPATH, '/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/div[8]').click()
            time.sleep(2)
            print("Done!")
        else:
            print("Not Following")
        time.sleep(2)


insta = SeleniumInstagramProje(username, password)
insta.login()
insta.getFollowers(100)
# insta.followUser("bestminimalsetup")
# insta.unfollowUser("bestminimalsetup")