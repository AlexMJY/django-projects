from flask import Flask
app = Flask(__name__)
# flask application을 생성하는 코드. __name__ 변수에 모듈명이 담긴다.
# 즉, pybo.py라는 모듈이 실행되는 것이므로 __name__ 변수에는 'pybo'라는 문자열이 담긴다.
# @app.route는 URL과 flask 코드를 매핑하는 데코레이터다. '/'이 요청되면 hello_pybo 함수를 실행시킨다.



@app.route('/')
def hello_pybo():
    return 'Hello, Pybo!'