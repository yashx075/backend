import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Database Configuration
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set in the environment variables.")

# Security Configuration
SECRET_KEY = os.getenv("SECRET_KEY")
if not SECRET_KEY:
    raise ValueError("SECRET_KEY is not set in the environment variables.")

ALGORITHM = "HS256"

# Token Expiry Configuration
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")
if ACCESS_TOKEN_EXPIRE_MINUTES is not None:
    try:
        ACCESS_TOKEN_EXPIRE_MINUTES = int(ACCESS_TOKEN_EXPIRE_MINUTES)
    except ValueError:
        raise ValueError("ACCESS_TOKEN_EXPIRE_MINUTES must be an integer.")
else:
    raise ValueError("ACCESS_TOKEN_EXPIRE_MINUTES is not set in the environment variables.")
