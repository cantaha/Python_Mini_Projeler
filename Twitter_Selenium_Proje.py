import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class TwitterProje:
    def __init__(self, username, password):
        self.driverOptions = webdriver.ChromeOptions()
        self.driverOptions.add_experimental_option("prefs", {"intl.accept_languages": "en.en-US,en;q=0.9,en;q=0"})
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(self.driverOptions)

    def login(self):
        self.driver.get("https://twitter.com/")
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[5]/a").click()
        time.sleep(3)
        loginInput = self.driver.find_element(By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input").send_keys(self.username, Keys.ENTER)
        time.sleep(3)
        passInput = self.driver.find_element(By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input").send_keys(self.password, Keys.ENTER)
        time.sleep(6)

    def getFollowers(self):
        self.followers = []
        self.driver.get("https://twitter.com/home")
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//*[@id='react-root']/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[9]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/div/div/div[4]/div[2]/a").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[1]/div[2]/nav/div/div[2]/div/div[2]/a").click()
        time.sleep(5)
        followersClass = self.driver.find_element(By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/section/div")
        followers = followersClass.find_elements(By.CSS_SELECTOR, ".css-175oi2r.r-1adg3ll.r-1ny4l3l")
        followersCount = len(followers)
        time.sleep(2)
        last_height = self.driver.execute_script("return 0, document.documentElement.scrollHeight;")
        print(followersCount)
        for user in followers:
            hrefText = user.find_element(By.TAG_NAME, "a").get_attribute("href")
            self.followers.append(hrefText)
            print(hrefText)

        while True:
            time.sleep(2)
            self.driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
            time.sleep(5)
            new_height = self.driver.execute_script("return 0, document.documentElement.scrollHeight;")
            followersClass = self.driver.find_element(By.XPATH,
                                                      "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/section/div")
            followers = followersClass.find_elements(By.CSS_SELECTOR, ".css-175oi2r.r-1adg3ll.r-1ny4l3l")
            for user in followers:
                hrefText = user.find_element(By.TAG_NAME, "a").get_attribute("href")
                if hrefText in self.followers:
                    pass
                else:
                    self.followers.append(hrefText)
                    print(hrefText)

            if new_height == last_height:
                print(followersCount)
                print(self.followers)
                break
            else:
                last_height = new_height
                continue

        with open("twit_users.txt", "w") as file:
            for user in self.followers:
                file.write(user + "\n")

        print(len(self.followers))

    def searchTweet(self, hashtag, counter):
        self.hashtag = []
        self.counter = counter
        self.driver.get(f"https://twitter.com/search?q=%23{hashtag}&src=typeahead_click")
        time.sleep(3)
        list = self.driver.find_elements(By.XPATH, "//div[@data-testid='tweetText']")
        print(len(list))
        for tweet in list:
            self.hashtag.append(tweet.text)
            print(tweet.text)
            print("*" * 10)

        time.sleep(2)
        last_height = self.driver.execute_script("return 0, document.documentElement.scrollHeight;")
        loop_counter = 0
        while True:
            if loop_counter > self.counter:
                break

            self.driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
            time.sleep(2)
            new_height = self.driver.execute_script("return 0, document.documentElement.scrollHeight;")

            list = self.driver.find_elements(By.XPATH, "//div[@data-testid='tweetText']")
            print(len(list))
            for tweet in list:
                if tweet in self.hashtag:
                    pass
                else:
                    self.hashtag.append(tweet.text)
                    print(tweet.text)
                    print("*" * 10)

            if last_height == new_height:
                break
            last_height = new_height
            loop_counter += 1


        with open("tweets.txt", "w", encoding="UTF-8") as file:
            for tweet in self.hashtag:
                file.write(str(tweet) + "\n")
                file.write("*" * 10 + "\n")

        print(len(list))


    def followUser(self, username):
        self.username = username
        self.driver.get(f"https://twitter.com/{self.username}")
        time.sleep(2)
        self.driver.find_element(By.XPATH,
                                 "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div[2]/div[1]/div[2]/div[3]/div[1]/div").click()
        time.sleep(2)
        self.driver.get("https://twitter.com")
        time.sleep(2)

    def unfollowUser(self, username):
        self.username = username
        self.driver.get(f"https://twitter.com/{self.username}")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div[2]/div[1]/div[2]/div[4]/div[1]/div").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div[2]/div[1]").click()
        time.sleep(2)
        self.driver.get("https:twitter.com")
        time.sleep(2)

# kullanıcı adı ve şifre girilmesi gerekli

username = "********"
password = "**************"
twit = TwitterProje(username, password)
twit.login()
twit.getFollowers()
twit.searchTweet("Learn Python", 1)
twit.followUser("**************")
twit.unfollowUser("**************")