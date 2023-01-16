# 라우터에 위와 같이 데이터를 조회하는 부분을 포함해도 문제는 없다. 
# 하지만 서로 다른 라우터에서 데이터를 처리하는 부분이 동일하여 중복될 수 있기 때문에 나눴다.
# 이 부분은 프로젝트 성격에 맞게 구현하면 된다.

from models import Question
from sqlalchemy.orm import Session


def get_question_list(db: Session):
    question_list = db.query(Question)\
        .order_by(Question.create_date.desc())\
        .all()
    return question_list