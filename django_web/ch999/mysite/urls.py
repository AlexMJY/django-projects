"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from mysite.views import HomeView
from mysite.views import UserCreateView, UserCreateDoneTV # UserCreateDoneTV는 계정 생성이 완료된 후에 보여줄 화면 처리

from django.conf.urls.static import static # 정적 파일 처리
from django.conf import settings # settings.py 모듈에서 정의한 항목들을 담고 있는 객체를 가리키는 reference


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')), # django의 기본 인증 URLconf를 가져와서 사용. 
    path('accounts/register/', UserCreateView.as_view(), name='register'),
    path('accounts/register/done/', UserCreateDoneTV.as_view(), name='register_done'),
    
    path('', HomeView.as_view(), name='home'),
    path('bookmark/', include('bookmark.urls')),
    path('blog/', include('blog.urls')),
    path('photo/', include('photo.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) # 기존 url 패턴에 static() 함수가 반환하는 url 패턴을 추가한다.
