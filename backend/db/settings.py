import os
from dotenv import load_dotenv


load_dotenv()

DB_HOST = os.getenv('HOST')
DB_USERNAME = os.getenv('USERNAME')
DB_PASSWORD = os.getenv('PASSWORD')
DB_NAME = os.getenv('DATABASE')
DEV_DB_NAME = os.getenv('DEV_DATABASE')
TEST_DB_NAME = os.getenv('TEST_DATABASE')
DB_PORT = os.getenv('PORT')

# define database url
DATABASE_URL = f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
TEST_DATABASE_URL = f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{TEST_DB_NAME}"
DEV_DATABASE_URL = f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DEV_DB_NAME}"




