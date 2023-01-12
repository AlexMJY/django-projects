# flask application을 생성하는 코드. __name__ 변수에 모듈명이 담긴다.
# 즉, pybo.py라는 모듈이 실행되는 것이므로 __name__ 변수에는 'pybo'라는 문자열이 담긴다.
# @app.route는 URL과 flask 코드를 매핑하는 데코레이터다. '/'이 요청되면 hello_pybo 함수를 실행시킨다.
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

# db 객체를 create_app 함수 안에서 생성하면 다른 모듈에서 사용할 수 없기 떄문에 밖에서 생성하고, 함수 내부에 등록한다.
db = SQLAlchemy()
migrate = Migrate()


def create_app(): # application factory
    app = Flask(__name__)
    app.config.from_object(config)
    
    # ORM
    db.init_app(app)
    migrate.init_app(app, db)
    from . import models

    # blueprint
    from .views import main_views, question_views, answer_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)
    
    return app