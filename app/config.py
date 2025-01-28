import os
from dotenv import load_dotenv

# Load environment variables from .env file if it exists
if os.path.exists(".env"):
    load_dotenv()
else:
    print("Warning: .env file not found. Using system environment variables.")

# Database Configuration
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:Ram77777%@localhost/tryquiz")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL is required but not set in environment variables or .env file.")

# Security Configuration
SECRET_KEY = os.getenv("SECRET_KEY", "32X4PTehAUy")
if not SECRET_KEY:
    raise ValueError("SECRET_KEY is required but not set in environment variables or .env file.")

ALGORITHM = "HS256"

# Token Expiry Configuration
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30)
try:
    ACCESS_TOKEN_EXPIRE_MINUTES = int(ACCESS_TOKEN_EXPIRE_MINUTES)
except ValueError:
    raise ValueError("ACCESS_TOKEN_EXPIRE_MINUTES must be an integer.")
