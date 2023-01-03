# 모델을 변경한 후에는 반드시 makemigrations와 migrate를 통해 데이터베이스를 변경해야 한다.

from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_dt = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self): # admin 사이트에 subject 보이기
        return self.subject
    
    
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_dt = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)