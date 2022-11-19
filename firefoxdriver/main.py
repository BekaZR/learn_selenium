from time import sleep

from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support import expected_conditions as exp
from selenium.webdriver.common.by import By

from json import load, dump

from os.path import exists

from core.settings import PATH, USERNAME, PASSWORD

from fake_useragent import UserAgent

from time import sleep

useragent = UserAgent() 

url = "https://www.instagram.com/"


class InstagramBot:
    driverpath = None

    def __init__(self) -> None:
        self.driver = Firefox(executable_path=self.driverpath)
    

    def login(self):
        self.driver.get(url)
        username = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.NAME, "username")))
        username.send_keys(USERNAME)
        
        sleep(1)
        
        password = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.NAME, "password")))
        password.send_keys(PASSWORD)
        
        sleep(1)
        
        login = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')))
        login.click()
        
        sleep(10)
        


    def like_on_post(self, url):
        try:
            self.driver.get(url)
            
            sleep(3)
            
            post = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div[1]/div[1]/article/div/div[2]/div/div[2]/section[1]/span[1]/button"))).click()
            
            sleep(2)
            
        except Exception as  e:
            print(e)
        
        finally:
            self.driver.close()
            self.driver.quit()