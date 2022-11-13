import os 


def create_media_directory():
    path = "/Users/user/Desktop/learn_selenium/media"
    os.makedirs(path, mode = 0o777, exist_ok = True)