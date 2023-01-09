from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm):
    email = forms.EmailField(label='이메일')
    
    class Meta:
        model = User
        fields = ("username", "password1", "password2", "email") # password2는 password1와 대조하는 값
        
'''
UserForm은 django.contrib.auth.forms 모듈의 UserCreationForm 클래스를 상속하여 만들었다. 
그리고 email 속성을 추가했다. UserForm을 따로 만들지 않고 UserCreationForm을
그대로 사용해도 되지만 위처럼 이메일 등의 속성을 추가하기 위해서는 UserCreationForm 클래스를 상속하여 만들어야 한다.
'''