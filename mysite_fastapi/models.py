from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from database import Base

# 모델을 생성했다면 SQLAlchemy의 alembic을 이용해 DB table을 생성한다.

class Question(Base):
    __tablename__ = "question"
    
    id = Column(Integer, primary_key=True) # can't be duplicated
    subject = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    create_date = Column(DateTime, nullable=False)
    
class Answer(Base):
    __tablename__ = "answer"
    
    id = Column(Integer, primary_key=True)
    content = Column(Text, nullable=False)
    create_date = Column(DateTime, nullable=False)
    question_id = Column(Integer, ForeignKey("question.id")) # question.id는 question 테이블의 id 컬럼을 의미
    # Answer모델에서 Question을 참조. relationship으로 속성을 생성하면 답변객체에서 연결된 질문의 제목을
    # answer.quesiton.subject처럼 참조할 수 있다.
    # Question은 참조 파라미터, backref는 역참조 파라미터다. 역참조는 답변을 거꾸로 참조하는 것을 의미한다.
    # 한 질문에 여러 개의 답변이 달릴 수 있는데, 역참조는 질문에 달린 답변들을 참조할 수 있게 한다.
    question = relationship("Question", backref="answers") 