import os

BAES_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BAES_DIR, 'pybo.db')) # db 접속 주소
SQLALCHEMY_TRACK_MODIFICATIONS = False # SQLAlchemy의 이벤트를 처리하는 옵션
SECRET_KEY = "dev"