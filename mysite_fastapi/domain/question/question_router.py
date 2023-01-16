# 해당 파일에 생성한 router 객체를 FastAPI 앱에 등록해야 한다. (main.py)

from fastapi import APIRouter

from database import SessionLocal
from models import Question

# 라우팅이란 FastAPI가 요청받은 URL을 해석하여 그에 맞는 함수를 실행하여 그 결과를 리턴하는 행위를 말한다.
router = APIRouter( 
    prefix="/api/quesiton",
)

@router.get("/list")
def question_list():
    db = SessionLocal()
    _question_list = db.query(Question).order_by(Question.create_date.desc()).all()
    db.close()
    return _question_list
    