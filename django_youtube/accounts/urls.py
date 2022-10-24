from . import views
from django.urls import path

app_name = 'accounts'


urlpatterns = [
    path('signup/', views.signup.as_view(), name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile, name='profile')
    
]
