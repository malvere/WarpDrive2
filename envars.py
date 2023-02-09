# ENV impots
import os
import socket

HOST = socket.gethostname()
if HOST.endswith(".local"):
    print(f"Running on local machine ({HOST})")
    from dotenv import load_dotenv

    load_dotenv("py.env")
else:
    print(f"Running on non-local machine ({HOST})")

""" !Add PROJECT_NAME in heroku Vars! """
API_TOKEN = str(os.getenv("API_TOKEN"))
PROJECT_NAME = os.getenv("PROJECT_NAME")
WEBHOOK_HOST = f"https://{PROJECT_NAME}.render.com"  # Enter here your link from Heroku project settings
WEBHOOK_URL_PATH = f"/{API_TOKEN}"
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_URL_PATH}"
WEBAPP_HOST = os.getenv("localhost")
WEBAPP_PORT = os.getenv("PORT")

CHANNEL_ID = os.getenv("CHANNEL_ID")
CALL_FILTERS = str(os.getenv("CALL_FILTERS")).split("\/")
ADMIN = os.getenv("ADMIN")

EMAIL_PWD = os.getenv("EMAIL_PWD")
EMAIL_LOGIN = os.getenv("EMAIL_LOGIN")
SMTP = os.getenv("SMTP")

url = os.getenv("DATABASE_URL")
