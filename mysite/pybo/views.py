from django.shortcuts import get_object_or_404, redirect, render
from .models import Question, Answer
from django.utils import timezone

def index(request):
    question_list = Question.objects.order_by('-create_dt')
    context = {'question_list' : question_list}
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    question = Question.objects.get(id = question_id)
    context = {'question' : question}
    return render(request, 'pybo/question_detail.html', context)

def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    question.answer_set.create(content=request.POST.get('content'), create_dt = timezone.now()) 
    # Question은 모델 Answer와 foreignkey로 연결되어 있기 때문에 위처럼 사용할 수 있다
    return redirect('pybo:detail', question_id=question.id) # 질문을 생성한 후 상세 화면을 다시 보여주기 위해 redirect 함수 사용
    