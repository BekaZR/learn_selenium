from time import sleep

from selenium import webdriver

from core.settings import PATH

url = "https://www.instagram.com/"

driver = webdriver.Chrome(executable_path=PATH)

def chrome():
    try:
        driver.get(url)
        sleep(5)
        driver.get("https://pypi.org/project/python-dotenv/")
        sleep(5)
    except Exception as e:
        print(e)
    finally:
        driver.close()
        driver.quit()