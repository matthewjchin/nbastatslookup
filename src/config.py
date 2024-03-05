import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DB_URI = os.environ.get("DATABASE_URL")


