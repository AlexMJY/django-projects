# database.py = DB settings file

# import contextlib

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./myapi.db" # db connect address

# create_engine is create connection pool
# it refers to making a certain nubmer of object that connect to DB and using them in rotation
# control the number of sessions to accessing the DB and to reduce the time required for session access
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread":False}
)

# Class to connect to DB
# autocommit=Falses는 데이터를 변경했을 때 commit을 해야지 실제 저장되도록 한다
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base() # Class used when configuring DB Model


# quesiton_router.py의 question_list함수를 보면 db 세션 객체를 생성하고 함수 종료 직전에
# 다시 db.close()를 호출한다. SQLAlchemy가 사용하는 커넥션 풀에 세션을 반환하기 위해서다.
# 대부분의 API는 db를 사용해야 하기 때문에 패턴으로 반복될 것이다. 
# Dependency Injection을 이용해 자동화한다. 
# @contextlib.contextmanager

def get_db(): # db 세션 객체를 리턴하는 제너레이터인 get_db 함수를 추가했다.
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()