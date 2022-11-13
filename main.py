from chromedriver.main import chrome

from core.services import create_media_directory


if __name__ == "__main__":
    
    create_media_directory()
    chrome()