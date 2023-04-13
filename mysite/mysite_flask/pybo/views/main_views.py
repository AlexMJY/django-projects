from flask import Blueprint, render_template, url_for
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/')
# __name__은 모듈명인 main.views가 인수로 전달된다. 첫 번째 파라미터인 main은 블루프린트의 별칭(Alias)이다.
# url_prefix는 라우팅 함수의 애너테이션 URL 앞에 기본으로 붙일 접두어 url을 의미한다.

@bp.route('/hello')
def hello_pybo():
    return 'Hello Pybo!'

@bp.route('/')
def index():
    return redirect(url_for('question._list'))