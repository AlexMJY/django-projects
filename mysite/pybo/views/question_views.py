from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from ..forms import QuestionForm
from ..models import Question


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
def question_vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user == question.author:
        messages.error(request, '본인이 작성한 글은 추천할수 없습니다')
    else:
        question.voter.add(request.user)
    return redirect('pybo:detail', question_id=question.id)