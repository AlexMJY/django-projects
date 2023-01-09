from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render

# from pybo.models import Question
from ..models import Question

from django.db.models import Q


def index(request):
    page = request.GET.get('page', '1') # GET방식으로 호출된 URL에서 page값을 가져온다. page값이 없이 호출된 경웨 default로 1을 설정
    kw = request.GET.get("kw", '') # 검색어
    question_list = Question.objects.order_by('-create_dt')
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) |  # 제목 검색
            Q(content__icontains=kw) |  # 내용 검색
            Q(answer__content__icontains=kw) |  # 답변 내용 검색
            Q(author__username__icontains=kw) |  # 질문 글쓴이 검색
            Q(answer__author__username__icontains=kw)  # 답변 글쓴이 검색
        ).distinct()
    # subject__icontains=kw의 의미는 제목에 kw 문자열이 포함되었는지를 의미한다.
    # filter 함수에서 모델 속성에 접근하기 위해서는 언더바 두개를 이용하여 하위 속성에 접근할 수 있다.
    # __contains 대신 __icontains를 사용하면 대소문자 가리지 않고 찾아 준다.
    
    paginator = Paginator(question_list, 10) # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page) # 요청된 페이지에 해당되는 객체 생성. 장고 내부적으로 데이터 전체를 조회하지 않고 해당 페이지의 데이터만 조회하도록 쿼리가 변경된다.
    context = {"question_list" : page_obj, "page" : page, "kw" : kw}
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    question = Question.objects.get(id = question_id)
    context = {'question' : question}
    return render(request, 'pybo/question_detail.html', context)