from http.client import HTTPResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import User
from django.contrib.auth import authenticate, login as loginsession


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
    if request.method == "GET":
        return render(request, "login.html")
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
    if user is not None:
        loginsession(request, user)
        return redirect('user:user')
    else:
        return HTTPResponse("로그인 실패")
        
def user(request):
    return HTTPResponse(request.user)


def profile(request, username):
    user = get_object_or_404(User, username=username)
    context = {
        "user":user
    }
    return render(request, 'profile.html', context)
    