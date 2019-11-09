from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import markdown
from django.shortcuts import render, get_object_or_404
from .models import Article

# def index(request):
#     return HttpResponse('欢迎访问我的博客首页')


def index(request):
    post_list = Article.objects.all()
    return render(request, 'blog/index.html', context={"post_list": post_list
                                                       })


def detail(request, pk):
    # detail 视图中解析markdown
    post = get_object_or_404(Article, pk=pk)
    post.body = markdown.markdown(
        post.body, extensions=[
            'markdown.extensions.extra', 'markdown.extensions.codehilite', 'markdown.extensions.toc', ])
    return render(request, 'blog/detail.html', context={'post': post})
