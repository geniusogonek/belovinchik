import os

from dotenv import load_dotenv

load_dotenv()

JWT_SECRET = str(os.getenv("JWT_SECRET"))
