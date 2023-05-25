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

""" !Add PROJECT_NAME in  enVars! """

""" Webhook """
API_TOKEN = str(os.getenv("API_TOKEN"))
PROJECT_NAME = os.getenv("PROJECT_NAME")
WEBHOOK_HOST = f"https://{PROJECT_NAME}.onrender.com"  # Enter here your link from Heroku project settings
WEBHOOK_URL_PATH = "/webhook"
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_URL_PATH}"
WEBAPP_HOST = os.getenv("localhost")
WEBAPP_PORT = os.getenv("PORT")

""" Administration and Restrictions """
CHANNEL_ID = os.getenv("CHANNEL_ID")  # Channel Id (bot should be added to it with admin priveleges)
CHANNEL_URL = os.getenv("CHANNEL_URL")  # Channel url to output for non-member users
CALL_FILTERS = str(os.getenv("CALL_FILTERS")).split(
    "\/"
)  # Filters CallBackCalls to be added to member-only list (see handlers.callback.tools for more info)
ADMIN = os.getenv("ADMIN")  # Get user which will have access for admin priveleges

""" Tools (such as WGCF bin) """
WGCF_BIN = os.getenv("WGCF")  # Determine WGCF_bin name

""" DataBase """

DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_NAME = os.getenv("DB_NAME")
DB_HOST = os.getenv("DB_HOST")
