# 해당 파일에 생성한 router 객체를 FastAPI 앱에 등록해야 한다. (main.py)

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from domain.question import question_schema
from models import Question

# 라우팅이란 FastAPI가 요청받은 URL을 해석하여 그에 맞는 함수를 실행하여 그 결과를 리턴하는 행위를 말한다.
router = APIRouter( 
    prefix="/api/quesiton",
)

# get_db함수의 finally에 작성한 db.close() 함수가 자동으로 실행된다.
@router.get("/list", response_model=list[question_schema.Quesiton])
def question_list(db: Session = Depends(get_db)):
    _question_list = db.query(Question).order_by(Question.create_date.desc()).all()
    return _question_list