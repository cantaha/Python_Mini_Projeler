import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

link = "https://www.linkedin.com/checkpoint/rm/sign-in-another-account?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin"
username = "tahacan107@gmail.com"
password = "************"
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
        self.wait = WebDriverWait(self.driver, 10)

    def login(self):
        self.driver.get(link)
        self.wait.until(EC.visibility_of_element_located((By.ID, "username"))).send_keys(self.username)
        self.wait.until(EC.visibility_of_element_located((By.ID, "password"))).send_keys(self.password, Keys.ENTER)
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[4]/aside[1]/div[1]/header/div[3]/button[2]'))).click()
        except:
            pass

    def jobsSearch(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='global-nav']/div/nav/ul/li[3]/a"))).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[4]/header/div/div/div/div[2]/div[2]/div/div/input[1]'))).send_keys(self.searchKeyword, Keys.ENTER)
        areaInput = self.wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[4]/header/div/div/div/div[2]/div[2]/div/div/input[1]')))
        areaInput.clear()
        areaInput.send_keys(self.areaKeyword, Keys.ENTER)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[3]/div[4]/section/div/section/div/div/div/ul/li[7]/div/button'))).click()

    def applyJob(self):
        self.appliedJobs = []
        while True:
            jobResults = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, '/html/body/div[4]/div[3]/div[4]/div/div/main/div/div[2]/div[1]/div/ul/li')))
            for job in jobResults:
                try:
                    jobTitle = job.find_element(By.XPATH, './/div[1]/div[2]/div[1]/a/strong').text
                    if jobTitle in ["Digital Marketing Specialist", "Dijital Pazarlama Uzmanı"] and jobTitle not in self.appliedJobs:
                        self.apply_to_job(jobTitle)
                except Exception as e:
                    print(f"İş ilanı işlenemedi: {e}")
                    continue
            # Sayfayı kaydırarak yeni ilanları yükleme
            try:
                next_button = self.driver.find_element(By.XPATH, "//button[@aria-label='Sayfa Sonraki']")
                if next_button.is_enabled():
                    next_button.click()
                    time.sleep(2)
                else:
                    break
            except:
                break

        with open("appliedJobs.txt", "w") as file:
            for job in self.appliedJobs:
                file.write(job + "\n")

    def apply_to_job(self, jobTitle):
        try:
            applyButton = self.wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div[3]/div[4]/div/div/main/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/div/div[1]/div[1]/div[4]/div/div/div/button')))
            applyButton.click()
            salaryInput = self.wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[2]/form/div/div/div/div/div/div[1]/div/input')))
            salaryInput.send_keys(self.expectedSalary, Keys.ENTER)
            sendApplyButton = self.wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[2]/div/footer/div[3]/button[2]')))
            sendApplyButton.click()
            self.appliedJobs.append(jobTitle)
            print(jobTitle)
        except Exception as e:
            print(f"{jobTitle} ilanına başvurulamadı: {e}")

linkedin = Linkedin(username, password, searchKeyword, areaKeyword, expectedSalary)
linkedin.login()
linkedin.jobsSearch()
linkedin.applyJob()