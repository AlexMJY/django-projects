# Pydantic은 FastAPI의 입출력 스펙을 정의하고 그 값을 검증하기 위해 사용하는 라이브러리이다.
# Pydantic은 API의 입출력 항목을 다음과 같이 정의하고 검증할수 있다.
# 1. 입출력 항목의 갯수와 타입을 설정
# 2. 입출력 항목의 필수값 체크
# 3. 입출력 항목의 데이터 검증

# Pydantic을 적용하기 위해서 가장 먼저 할 일은 질문 목록 API의 출력 스키마를 생성하는 것이다.
# 스키마는 프로그래밍 세계에서 보통 데이터의 구조와 명세를 의미한다.
# 즉, 출력 스키마라고 하면 출력 항목이 몇 개인지, 제약 조건은 어떤한 것이 있는지 등을 기술하는 것을 말한다.
# 질문과 관련된 API의 스키마는 question 도메인 디렉터리에 question_schema.py 파일에서 관리한다.

import datetime

from pydantic import BaseModel


class Question(BaseModel):
    id: int
    subject: str
    content: str
    create_date: datetime.datetime

    class Config:
        orm_mode = True