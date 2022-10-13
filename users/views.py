from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import User

# Create your views here.
def sign_up(request):
    if request.method == "GET":
        return render(request, "sign_up.html")
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        password_check = request.POST.get("password_check")
        if password == password_check:
            User.objects.create_user(username = username, password = password, password_check = password_check)
            return HTTPResponse("회원가입 완료")

            
        else:
            return HTTPResponse("비번 오류")
        
    else:    
        return HttpResponse("허용되지 않는 메소드입니다.")
    
    
def login(request):
    return HTTPResponse("로그인 페이지")