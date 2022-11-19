from firefoxdriver.main import InstagramBot

from core.services import create_media_directory


if __name__ == "__main__":
    InstagramBot.driverpath = "/Users/user/Desktop/learn_selenium/firefoxdriver/geckodriver"
    instagram = InstagramBot()
    instagram.login()

    instagram.like_on_post("https://www.instagram.com/p/ClH2HB8pIU_/")