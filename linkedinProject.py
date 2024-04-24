import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

link = "https://www.linkedin.com/"
username = "*********"
password = "********"
searchKeyword = "Digital Marketing"
areaKeyword = "İstanbul, Türkiye"
expectedSalary = "50000 TL"

class Linkedin:
    def __init__(self, username, password, searchKeyword, areaKeyword, expectedSalary):
        self.driverOptions = webdriver.ChromeOptions()
        self.driverOptions.add_experimental_option("prefs", {"intl.accept_languages": "en.en-US,en;q=0.9,en;q=0"})
        self.username = username
        self.password = password
        self.searchKeyword = searchKeyword
        self.areaKeyword = areaKeyword
        self.expectedSalary = expectedSalary
        self.driver = webdriver.Chrome(self.driverOptions)

    def login(self):
        self.driver.get(link)
        time.sleep(2)
        usernameInput = self.driver.find_element(By.XPATH, "//*[@id='session_key']").send_keys(self.username)
        time.sleep(2)
        passwordInput = self.driver.find_element(By.XPATH, "//*[@id='session_password']").send_keys(self.password, Keys.ENTER)
        time.sleep(2)
        messageCloseButton = self.driver.find_element(By. XPATH, '/html/body/div[4]/div[4]/aside[1]/div[1]/header/div[3]/button[2]').click()
        time.sleep(2)

    def jobsSearch(self):
        time.sleep(2)
        jobsButton = self.driver.find_element(By.XPATH, "//*[@id='global-nav']/div/nav/ul/li[3]/a").click()
        time.sleep(5)
        searchInput = self.driver.find_element(By.XPATH, '/html/body/div[4]/header/div/div/div/div[2]/div[2]/div/div/input[1]').send_keys(self.searchKeyword, Keys.ENTER)
        time.sleep(4)
        areaInput = self.driver.find_element(By.XPATH, '/html/body/div[4]/header/div/div/div/div[2]/div[2]/div/div/input[1]').clear()
        time.sleep(3)
        areaInput2 = self.driver.find_element(By.XPATH, '/html/body/div[4]/header/div/div/div/div[2]/div[2]/div/div/input[1]').send_keys(self.areaKeyword, Keys.ENTER)
        time.sleep(4)
        easyApplyButton = self.driver.find_element(By.XPATH, '/html/body/div[4]/div[3]/div[4]/section/div/section/div/div/div/ul/li[7]/div/button').click()
        time.sleep(4)

    def applyJob(self):
        self.appliedJobs = []
        time.sleep(2)
        jobResults = self.driver.find_element(By.XPATH, '/html/body/div[4]/div[3]/div[4]/div/div/main/div/div[2]/div[1]/div/ul')
        jobs = jobResults.find_elements(By.TAG_NAME, 'li' )
        jobResultsCount = len(jobs)
        print(jobResultsCount)
        time.sleep(2)
        lastHeight = self.driver.execute_script("return 0, document.body.scrollHeight;")
        for job in jobs:
            jobTitle = job.find_element(By.XPATH, '/html/body/div[4]/div[3]/div[4]/div/div/main/div/div[2]/div[1]/div/ul/li[1]/div/div/div[1]/div[2]/div[1]/a/strong').text
            if jobTitle == "Digital Marketing Specialist":
                applyButton = self.driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div[4]/div/div/main/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/div/div[1]/div[1]/div[4]/div/div/div/button').click()
                time.sleep(2)
                applyButton2 = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button').click()
                time.sleep(3)
                applyButton3 = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button[2]').click()
                time.sleep(2)
                salaryInput = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[2]/form/div/div/div/div/div/div[1]/div/input').send_keys(self.expectedSalary, Keys.ENTER)
                time.sleep(3)
                sendApplyButton = self.driver.find_element(By. XPATH, '/html/body/div[3]/div/div/div[2]/div/div[2]/div/footer/div[3]/button[2]').click()
                time.sleep(3)
                if jobTitle in self.appliedJobs:
                    pass
                else:
                    self.appliedJobs.append(jobTitle)
                    print(jobTitle)

        while True:
            time.sleep(2)
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
            newHeight = self.driver.execute_script("return 0, document.body.scrollHeight;")
            jobResults = self.driver.find_element(By.XPATH, '/html/body/div[4]/div[3]/div[4]/div/div/main/div/div[2]/div[1]/div/ul')
            time.sleep(2)
            jobs = jobResults.find_elements(By.TAG_NAME, 'li' )
            time.sleep(2)
            for job in jobs:
                jobTitle = job.find_element(By.XPATH, '/html/body/div[4]/div[3]/div[4]/div/div/main/div/div[2]/div[1]/div/ul/li[1]/div/div/div[1]/div[2]/div[1]/a/strong').text
                if jobTitle == "Digital Marketing Specialist" or jobTitle == "Dijital Pazarlama Uzmanı" and jobTitle not in self.appliedJobs:
                    applyButton = self.driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div[4]/div/div/main/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/div/div[1]/div[1]/div[4]/div/div/div/button').click()
                    time.sleep(2)
                    applyButton2 = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button').click()
                    time.sleep(3)
                    applyButton3 = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button[2]').click()
                    time.sleep(2)
                    salaryInput = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[2]/form/div/div/div/div/div/div[1]/div/input').send_keys(self.expectedSalary, Keys.ENTER)
                    time.sleep(3)
                    sendApplyButton = self.driver.find_element(By. XPATH, '/html/body/div[3]/div/div/div[2]/div/div[2]/div/footer/div[3]/button[2]').click()
                    time.sleep(3)
                    if jobTitle in self.appliedJobs:
                        pass
                    else:
                        self.appliedJobs.append(jobTitle)
                        print(jobTitle)

            if newHeight == lastHeight:
                print(jobResultsCount)
                print(self.appliedJobs)
                break
            else:
                lastHeight = newHeight
                continue

        with open("appliedJobs.txt", "w") as file:
            for job in self.appliedJobs:
                file.write(job + "\n")



linkedin = Linkedin(username, password, searchKeyword, areaKeyword, expectedSalary)
linkedin.login()
linkedin.jobsSearch()
linkedin.applyJob()