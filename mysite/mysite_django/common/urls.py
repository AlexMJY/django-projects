from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = "common"

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
]

'''
LoginView는 registration이라는 템플릿 디렉터리에서 login.html 파일을 찾는다. 
그런데 이 파일을 찾지 못해 오류가 발생한 것이다. 
이 오류를 해결하려면 registration/login.html 템플릿 파일을 작성해야 한다.

하지만 로그인은 common 앱에 구현할 것이므로 오류 메시지에 표시한 것처럼 
registration 디렉터리에 템플릿 파일을 생성하기보다는 common 디렉터리에 템플릿을 생성하는 것이 좋다.

as_view() 안에 html파일의 위치를 지정해주면 된다.
'''

'''
django.contrib.auth패키지는 디폴트로 /accounts/profile/ URL로 이동시키기 때문에 오류가 발생한다.
로그인 성공 시 / 페이지로 이동할 수 있도록 config/settings.py 파일을 수정해야 한다.
config/settings 파일에 LOGIN_REDIRECT_URL을 추가하면 된다.
'''