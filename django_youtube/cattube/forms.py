from django import forms
from .models import Video, Comment

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = "__all__"
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = "__all__"        