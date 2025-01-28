from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    username: str
    password: str

class UserLogin(UserBase):
    password: str

class UserOut(UserBase):
    id: int
    class Config:
        orm_mode = True

class QuestionOut(BaseModel):
    id: int
    question: str
    option_a: str
    option_b: str
    option_c: str
    option_d: str
    correct_answer: int
    class Config:
        orm_mode = True