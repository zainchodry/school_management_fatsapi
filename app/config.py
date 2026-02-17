from pydantic_settings import BaseSettings
import os

# project root
ENV_PATH = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
BASE_DIR = os.path.join(ENV_PATH, '.env')


class Settings(BaseSettings):
    SQLALCHEMY_DATABASE_URI: str
    SECRET_KEY: str
    ALGORITHM: str
    PROJECT_NAME: str = "School Management System FastApi"

    class Config:
        # point to the .env file in project root
        env_file = BASE_DIR
        env_file_encoding = 'utf-8'


settings = Settings()