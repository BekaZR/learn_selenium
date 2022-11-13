from time import sleep

from selenium import webdriver

from core.settings import PATH

url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent/"

options = webdriver.ChromeOptions()

options.add_argument("user-agent=Helloworld:)")

driver = webdriver.Chrome(executable_path=PATH, options=options)

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