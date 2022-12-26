from django.shortcuts import render
from .models import Question, Answer

def index(request):
    question_list = Question.objects.order_by('-create_dt')
    context = {'question_list' : question_list}
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    question = Question.objects.get(id = question_id)
    context = {'question' : question}
    return render(request, 'pybo/question_detail.html', context)