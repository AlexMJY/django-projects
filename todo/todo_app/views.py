from typing import Any
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse
from .models import ToDoList, ToDoItem

class ListListView(ListView):
    model = ToDoList
    template_name = "todo_app/index.html"
    
class ItemListView(ListView):
    model = ToDoItem
    template_name = 'todo_app/todo_list.html'
    
    # 클래스가 생성될 때 list_id라는 키워드 인수가 클래스에 전달되어야 아래 두 개의 메서드에 나오는 self.kwargs["list_id"]에 적용된다
    
    # 반환되는 데이터를 필터링(정제)
    # html에 넘겨지는 object_list 키에 적용된다
    def get_queryset(self):
        return ToDoItem.objects.filter(todo_list_id=self.kwargs["list_id"])
    
    # 렌더링에 사용할 수 있는 데이터를 필터링
    # super()로 상위 객체를 먼저 호출해야 새 데이터가 기존 컨텍스트를 덮어버리지 않고 병합할 수 있다
    def get_context_data(self):
        context = super().get_context_data()
        context["todo_list"] = ToDoList.objects.get(id=self.kwargs["list_id"])
        return context
    

class ListCreate(CreateView):
    model = ToDoList
    fields = ["title"]
    
    def get_context_data(self):
        context = super(ListCreate, self).get_context_data()
        context["title"] = "Add a new list"
        return context
    
class ItemCreate(CreateView):
    model = ToDoItem
    fields = [
        "todo_list",
        "title",
        "description",
        "due_date",
    ]
    def get_initial(self):
        initial_data = super(ItemCreate, self).get_initial()
        todo_list = ToDoList.objects.get(id=self.kwargs["list_id"])
        initial_data["todo_list"] = todo_list
        return initial_data
    
    def get_context_data(self):
        context = super(ItemCreate, self).get_context_data()
        todo_list = ToDoList.objects.get(id=self.kwargs["list_id"])
        context["todo_list"] = todo_list
        context["title"] = "Create a new item"
        return context
    
    def get_success_url(self) -> str:
        return reverse("list", args=[self.object.todo_list_id])
        

class ItemUpdate(UpdateView):
    model = ToDoItem
    fields = [
        "todo_list",
        "title",
        "description",
        "due_date",
    ]
    
    def get_context_data(self):
        context = super(ItemUpdate, self).get_context_data()
        context["todo_list"] = self.object.todo_list
        context["title"] = "Edit item"
        return context
    
    def get_success_url(self) -> str:
        return reverse("list", args=[self.object.todo_list_id])