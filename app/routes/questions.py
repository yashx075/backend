from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import models, schemas, database

router = APIRouter(prefix="/questions", tags=["questions"])

@router.get("/", response_model=list[schemas.QuestionOut])
def get_questions(db: Session = Depends(database.get_db)):
    questions = db.query(models.Question).all()
    return questions
