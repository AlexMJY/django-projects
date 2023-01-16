# 라우터 파일에 반드시 필요한 것은 APIRouter 클래스로 생성한 router 객체이다.
# 해당 파일에 생성한 router 객체를 FastAPI 앱에 등록해야 한다. (main.py)
# 라우팅이란 FastAPI가 요청받은 URL을 해석하여 그에 맞는 함수를 실행하여 그 결과를 리턴하는 행위를 말한다.


from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from domain.question import question_schema, question_crud
# from models import Question -> question_crud로 대체

# 라우팅이란 FastAPI가 요청받은 URL을 해석하여 그에 맞는 함수를 실행하여 그 결과를 리턴하는 행위를 말한다.
router = APIRouter( 
    prefix="/api/question",
)

# get_db함수의 finally에 작성한 db.close() 함수가 자동으로 실행된다.
@router.get("/list", response_model=list[question_schema.Question])
def question_list(db: Session = Depends(get_db)):
    # _question_list = db.query(Question).order_by(Question.create_date.desc()).all()
    _question_list = question_crud.get_question_list(db)
    return _question_list