from django.utils import timezone

from django.db import models
from django.urls import reverse

# 기한 설정을 하는 독립적 함수
def one_week_hence():
    return timezone.now() + timezone.timedelta(days=7)

class ToDoList(models.Model):
    title = models.CharField(max_length=100, unique=True)
    
    def get_absolute_url(self):
        return reverse("list", args=[self.id])
    
    def __str__(self) -> str:
        return self.title
    
class ToDoItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(default=one_week_hence) # one_week_hence() 사용하여 기본 마감일을 일주일 후로 설정 / 사용자가 마감일 변경 가능
    todo_list = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    

    class Meta: # 메타 클래스로 옵션 설정 가능 
        ordering = ["due_date"] # 클래스의 레코드 기본 순서 설정

    def __str__(self):
        return f"{self.title}: due{self.due_date}"

    def get_absolute_url(self): # 하드코딩 하지않고 링크에 접근할 수 있도록 도와줌
        return reverse("item-update", args=[str(self.todo_list.id), str(self.id)])

    