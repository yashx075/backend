# Wexa Quiz Backend

Welcome to the **Wexa Quiz Backend**! This backend powers a quiz application that allows users to register, log in, and participate in quizzes. The application is built with **FastAPI** and provides secure endpoints for authentication, user management, and quiz functionalities.

---

## Features

- **User Authentication**: Secure registration and login using JWT.
- **Quiz Management**: Fetch quiz questions and validate answers.
- **Score Tracking**: Keep track of quiz scores.
- **RESTful API**: Well-structured and easy-to-use endpoints.

---

## Tech Stack

- **Framework**: [FastAPI](https://fastapi.tiangolo.com/)
- **Database**: PostgreSQL (or your configured database)
- **Authentication**: JSON Web Tokens (JWT)
- **Hosting**: Deployed on [Render](https://render.com/)

---

## API Documentation

The API documentation is available at `/docs` once the server is running.

---

## Installation

Follow these steps to set up and run the backend application:

### 1. Clone the repository

```bash
git clone https://github.com/yashx075/backend_wexa.git
cd backend_wexa
2. Create a virtual environment and activate it
python -m venv venv
source venv/bin/activate  # For Linux/MacOS
venv\Scripts\activate     # For Windows
3. Install dependencies
pip install -r requirements.txt
4. Set up the environment variables
Create a .env file in the project root and add the following:
DATABASE_URL=postgresql://username:password@localhost:5432/database_name
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
Replace username, password, and localhost:5432/database_name with your database credentials.
Replace your-secret-key with a strong, random secret key.
5. Run database migrations
If you're using a migration tool like Alembic, run:
alembic upgrade head
Or manually initialize the database schema.
6. Start the server
uvicorn main:app --reload
The server will start at http://127.0.0.1:8000.
Endpoints
Authentication
POST /auth/register: Register a new user.
POST /auth/login: Log in to get a JWT token.
Quiz
GET /quiz/questions: Fetch a list of quiz questions.
POST /quiz/submit: Submit quiz answers and calculate the score.
User
GET /user/profile: Get the logged-in user's profile (requires JWT token).
Deployment
The backend is deployed on Render. You can access the production API at:
https://backend-wexa.onrender.com
To deploy your own version:
Push your code to a GitHub repository.
Connect the repository to Render.
Add environment variables in the Render dashboard.
Deploy the backend.
Testing
Run the test suite to ensure everything works as expected:
pytest
Folder Structure
backend_wexa/
├── app/
│   ├── main.py         # Main application entry point
│   ├── models/         # Database models
│   ├── routers/        # API route handlers
│   ├── schemas/        # Request/response models
│   ├── utils/          # Utility functions
│   ├── database.py     # Database connection setup
├── migrations/         # Database migration files
├── requirements.txt    # Python dependencies
├── .env                # Environment variables
├── README.md           # Project documentation
How to Use
Register: Create an account via /auth/register.
Login: Log in via /auth/login to get your JWT token.
Start Quiz: Use the token to access /quiz/questions and submit your answers to /quiz/submit.
Contributing
We welcome contributions! Please follow these steps:
Fork the repository.
Create a feature branch: git checkout -b feature-name.
Commit your changes: git commit -m 'Add a feature'.
Push to your branch: git push origin feature-name.
Submit a pull request.



### Customize:
- Replace placeholders like `your-username`, `your-secret-key`, and email addresses with actual details.
- If you use additional tools or features, document them in relevant sections.

Let me know if you'd like help tailoring this further!



