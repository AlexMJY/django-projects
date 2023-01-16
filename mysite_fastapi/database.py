# database.py = DB settings file

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