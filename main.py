from dotenv import load_dotenv
from fastapi import FastAPI
from app.database import engine
from app.models import Base
from app.routes import auth, questions
from fastapi.middleware.cors import CORSMiddleware

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI()

# Create database tables
Base.metadata.create_all(bind=engine)

# Include routes
app.include_router(auth.router)
app.include_router(questions.router)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update with your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Welcome to the FastAPI application!"}