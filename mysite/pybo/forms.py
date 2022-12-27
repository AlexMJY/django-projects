from django import forms
from pybo.models import Question, Answer

# forms.Form과 forms.ModelForm이 있는데 모델 폼은 연결된 모델의 데이터를 저장할 수 있다.
# 모델 폼은 inner Class인 Meta 클래스가 반드시 필요하다. 사용할 모델과 모델의 속성을 적는다

class QuestionForm(forms.ModelForm):
    class Meta: 
        model = Question # 사용할 모델
        fields = ['subject', 'content'] # 사용할 Question 모델의 속성
        # widgets = { # form.as_p 때문에 적용못하던 부트스트랩 클래스를 필드에 적용할 수 있다.
        #     'subject' : forms.TextInput(attrs={'class' : 'form-control'}),
        #     'content' : forms.Textarea(attrs={'class' : 'form-control', 'rows':10 })
        # }
        labels = {
            'subject' : '제목',
            'content' : '내용',
        }
        
class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content' : '답변내용',
        }