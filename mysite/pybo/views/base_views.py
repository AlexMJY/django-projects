from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render

# from pybo.models import Question
from ..models import Question


def index(request):
    page = request.GET.get('page', '1') # GET방식으로 호출된 URL에서 page값을 가져온다. page값이 없이 호출된 경웨 default로 1을 설정
    question_list = Question.objects.order_by('-create_dt')
    paginator = Paginator(question_list, 10) # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page) # 요청된 페이지에 해당되는 객체 생성. 장고 내부적으로 데이터 전체를 조회하지 않고 해당 페이지의 데이터만 조회하도록 쿼리가 변경된다.
    context = {'question_list' : page_obj}
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    question = Question.objects.get(id = question_id)
    context = {'question' : question}
    return render(request, 'pybo/question_detail.html', context)