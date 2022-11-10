from dotenv import dotenv_values

config = dotenv_values(".env")

PATH = config.get('PATH')