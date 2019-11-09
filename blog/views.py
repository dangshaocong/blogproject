from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Article

# def index(request):
#     return HttpResponse('欢迎访问我的博客首页')


def index(request):
    post_list = Article.objects.all()
    return render(request, 'blog/index.html', context={"post_list": post_list
                                                       })
def detail(request, pk):
    post = get_object_or_404(Article, pk=pk)
    return render(request, 'blog/detail.html', context={'post': post})
