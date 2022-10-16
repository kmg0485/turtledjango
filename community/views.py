from http.client import HTTPResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Article

# Create your views here.

def index(request):
    articles = Article.objects.all().order_by('-created_at')
    context={
        "articeles" : articles
    }
    
    return render(request, "index.html", context)
    
    
def create_article(request):
    if request.method == "GET":
        return render(request, "create_article.html")
    
    elif request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        user = request.user
        Article.objects.create(title=title, content=content, user=user)
        
        return redirect("community:index")
    

def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    context = {
        "article":article
    }
    return render(request, 'article_detail.html', context)
        