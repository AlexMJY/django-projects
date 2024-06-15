# from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Bookmark

from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin # @login_required() 데코레이터 기능을 적용할 때 사용. 사용자가 로그인 된 경우 정상 처리하게 한다. 로그인이 안된 사용자는 로그인 페이지로 리다이렉트
from django.urls import reverse_lazy # urlconf 패턴화 == 하드코딩 하지 않아도 됨
from mysite.views import OwnerOnlyMixin

class BookmarkLV(ListView):
    model = Bookmark
    
class BookmarkDV(DetailView):
    model = Bookmark
    

class BookmarkCreateView(LoginRequiredMixin, CreateView):
    model = Bookmark
    fields = ['title', 'url']
    success_url = reverse_lazy('bookmark:index')
    
    def form_valid(self, form): # 폼에 입력된 내용을 유효성 검사해서 에러가 없는 경우 form_valid 메소드를 호출한다.
        form.instance.owner = self.request.user # 모델 객체의 owner 필드에 현재 로그인된 사용자의 User 객체를 할당
        return super().form_valid(form) # DB에 반영되고 그 후 success_url로 리다이렉트

class BookamrkChangeLV(LoginRequiredMixin, ListView):
    template_name = 'bookmark/bookmark_change_list.html'
    
    def get_queryset(self): # 화면에 출력할 레코드 리스트 반환.
        return Bookmark.objects.filter(owner=self.request.user)  
    

class BookmarkUpdateView(OwnerOnlyMixin, UpdateView):
    model = Bookmark
    fields = ['title', 'url']
    success_url = reverse_lazy('bookmark:index')

class BookmarkDeleteView(OwnerOnlyMixin, DeleteView):
    model = Bookmark
    success_url = reverse_lazy('bookmark:index')