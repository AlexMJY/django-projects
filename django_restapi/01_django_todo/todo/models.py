from django.db import models

class Todo(models.Model):
    # django가 기본으로 제공하는 pk인 id 필드도 포함되어 있다.
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=False)
    complete = models.BooleanField(default=False)
    important = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title