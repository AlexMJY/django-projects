from django.shortcuts import render

from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from books.models import Book, Author, Publisher


# TemplateView
class BooksModelView(TemplateView):
    template_name = 'books/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_list'] = ['Book', 'Author', 'Publisher'] # 애플리케이션 첫 화면에 테이블 리스트를 보여주기 위해 model_list에 담아서 템플릿 시스템에 넘겨준다.
        return context

# ListBiew
class BookList(ListView):
    model = Book
    
class AuthorList(ListView):
    model = Author
    
class PublisherList(ListView):
    model = Publisher
    
# DetailView
class BookDetail(DetailView):
    model = Book
    
class AuthorDetail(DetailView):
    model = Author
    
class PublisherDetail(DetailView):
    model = Publisher