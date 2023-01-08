from django.shortcuts import get_object_or_404, redirect, render
from .models import Question, Answer
from django.utils import timezone
from .forms import QuestionForm, AnswerForm
from django.http import HttpResponseNotAllowed
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages

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

@login_required(login_url='common:login') # 아래의 함수는 로그인이 필요하다.
def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user # # author 속성에 로그인 계정 저장. request.user는 현재 로그인한 계정의 User 모델 객체이다.
            answer.create_dt = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question.id) # 질문을 생성한 후 상세 화면을 다시 보여주기 위해 redirect 함수 사용
    else:
        form = AnswerForm()
    context = {'question' : question, 'form' : form}
    return render(request, 'pybo/question_detail.html', context)

@login_required(login_url='common:login') # 아래의 함수는 로그인이 필요하다.
def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid(): # 폼이 유효하다면
            question = form.save(commit=False) # 임시 저장하여 question 객체를 리턴받는다.
            question.author = request.user
            question.create_dt = timezone.now() # 실제 저장을 위해 작성일시를 설정한다.
            question.save() # 데이터를 실제로 저장한다.
            return redirect('pybo:index')
    else:
        form = QuestionForm()
    context = {'form' : form}
    return render(request, 'pybo/question_form.html', context)

@login_required(login_url='common:login')
def question_modify(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('pybo:detail', question_id=question.id)
    if request.method == "POST":
        # instance를 기준으로 QuestionForm을 생성하지만 request.POST의 값으로 덮어쓰라는 의미이다. 
        # 따라서 질문 수정화면에서 제목 또는 내용을 변경하여 POST 요청하면 변경된 내용이 QuestionForm에 저장될 것이다.
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.modify_date = timezone.now()  # 수정일시 저장
            question.save()
            return redirect('pybo:detail', question_id = question.id)
    else:
        # 폼 생성시 instance를 지정하면 폼의 속성 값이 instance의 값으로 채워진다. 질문을 수정하는 화면에서 제목과 내용이 채워진 채로 보일 것이다.
        form = QuestionForm(instance=question)
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)
'''
question_modify 함수는 로그인한 사용자(request.user)와 수정하려는 질문의 글쓴이(question.author)가 
다를 경우에는 "수정권한이 없습니다"라는 오류를 발생시킨다. 이 오류를 발생시키기 위해 messages 모듈을 이용하였다. 
messages는 장고가 제공하는 모듈로 넌필드 오류(non-field error)를 발생시킬 경우에 사용한다.
'''

@login_required(login_url='common:login')
def question_delete(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('pybo:detail', question_id=question.id)
    question.delete()
    return redirect('pybo:index')

@login_required(login_url='common:login')
def answer_modify(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('pybo:detail', question_id=answer.question.id)
    if request.method == "POST":
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.modify_date = timezone.now()
            answer.save()
            return redirect('pybo:detail', question_id=answer.question.id)
    else:
        form = AnswerForm(instance=answer)
    context = {'answer': answer, 'form': form}
    return render(request, 'pybo/answer_form.html', context)

@login_required(login_url='common:login')
def answer_delete(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, '삭제권한이 없습니다.')
    else:
        answer.delete()
    return redirect('pybo:detail', question_id = answer.question.id)