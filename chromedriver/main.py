from time import sleep

from selenium import webdriver

from core.settings import PATH

url = "https://www.instagram.com/"

driver = webdriver.Chrome(executable_path=PATH)

def chrome():
    try:
        driver.get(url)
        sleep(5)
        driver.get_screenshot_as_file("1.png")
        driver.save_screenshot('2.png')
        sleep(5)
        
    except Exception as e:
        print(e)
    finally:
        driver.close()
        driver.quit()