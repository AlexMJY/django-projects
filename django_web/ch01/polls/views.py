from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Question, Choice

import logging
logger = logging.getLogger(__name__)
# polls.views 로거 객체를 취득한다. __name__은 모듈 경로를 담고 있는 파이썬 내장 변수다. 즉 views.py 파일의 모듈 경로는 polls.views이고 
# 사용하고자 하는 로거 객체의 이름이다. 이 로거에서 생산한 로그 레코드는 상위 polls 로거에게 전파되고 polls 로거에서 메시지를 기록한다.


# def index(request):
#     latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
#     context = {'latest_question_list' : latest_question_list}
#     return render(request, 'polls/index.html', context)

# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question':question})

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list' # 컨테스트 변수명을 디폴트로 사용하지 않고 따로 지정. 디폴트 컨텍스트 변수명은 object_list와 question_list 둘 다 가능
    def get_queryset(self):
        # 최근 생성된 질문 5개 반환
        return Question.objects.order_by('-pub_date')[:5]
    
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    
class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    # logger.debug(f"vote().question_id: {question.id}")
    # 로거 객체의 degug() 메소드를 호출하여 로거에게 DEBUG 수준으로 로그 레코드를 생성하도록 요청한다.
    # 로거는 settings.py의 로깅 설정에 따라 file 핸들러를 사용하여 ch99/logs/mysite.log 파일에 로그 메시지를 기록한다.
    question = get_object_or_404(Question, pk=question_id)
    try:
        seleted_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # 설문 투표 폼을 다시 보여준다
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else: # 정상 처리 되었을 경우
        seleted_choice.votes += 1
        seleted_choice.save()
        # POST 데이터를 정상처리 했으면, HttpResponseRedirect를 반환하여 리다이렉션 처리
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
    # URLconf는 일반적으로 URL 스트링과 뷰를 매핑한 각 라인을 URL 패턴이라 하고 이름을 하나씩 부여한다.
    # 그러나 반대 방향으로 reverse() 함수를 사용하여 URL 패턴명으로 URL 스트링을 구할 수도 있다. 하드코딩하지 않아도 된다.
    
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question':question})