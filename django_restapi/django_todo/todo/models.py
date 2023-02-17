from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    importance = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title