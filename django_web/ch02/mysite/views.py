from django.views.generic import TemplateView

from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy # 인자로 URL 패턴명을 받는다. 


from django.contrib.auth.mixins import AccessMixin

#-- Homepage View
class HomeView(TemplateView):
    template_name = 'home.html'
    
    
#-- User Creation
class UserCreateView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register_done')
    
class UserCreateDoneTV(TemplateView):
    template_name = 'registration/register_done.html'
    
    
class OwnerOnlyMixin(AccessMixin):
    raise_exception = True
    permission_denied_message = "Owner only can update/delete the object"
    
    def dispatch(self, request, *args, **kwargs): # 메인 메소드인 get() 이전 단계의 dispatch() 메소드를 오버라이딩 (dispath -> get/post). 여기서 소유자 여부를 판단.
        obj = self.get_object()
        if request.user != obj.owner:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)
    