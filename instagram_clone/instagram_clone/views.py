from django.shortcuts import render
from rest_framework.views import APIView

class Sub(APIView):
    def get(self, request):
        print('request GET')
        return render(request, "instagram_clone/main.html")
    
    def post(self, request):
        print('request POST')
        return render(request, "instagram_clone/main.html")