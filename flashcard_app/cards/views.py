from typing import Any, Dict
from django.db.models.query import QuerySet
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy

from .models import Card

class CardListView(ListView):
    model = Card
    queryset = Card.objects.all().order_by("box", "-date_created")
    
    
class CardCreateView(CreateView):
    model = Card
    fields = ["question", "answer", "box"]
    success_url = reverse_lazy("card-create")

class CardUpdateView(CardCreateView, UpdateView):
    success_url = reverse_lazy("card-list")
    
    
class BoxView(CardListView):
    template_name = "cards/box.html"
    
    def get_queryset(self) -> QuerySet[Any]:
        return Card.objects.filter(box=self.kwargs["box_num"])
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["box_number"] = self.kwargs["box_num"]
        return context