# from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Bookmark

class BookmarkLV(ListView):
    model = Bookmark
    
class BookmarkDV(DetailView):
    model = Bookmark