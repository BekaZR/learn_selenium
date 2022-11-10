import time

from selenium import webdriver
from core.settings import PATH




url = "https://www.instagram.com/"

driver = webdriver.Chrome(executable_path=PATH)

try:
    driver.get(url=url)
    time.sleep(5)
except Exception as e:
    print(e)
finally:
    driver.close()
    driver.quit()
