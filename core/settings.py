from dotenv import dotenv_values

env = dotenv_values(".env")

PATH = env.get('PATH')