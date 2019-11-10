from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import markdown
import re
from django.shortcuts import render, get_object_or_404
from .models import Article, Category, Tag
# blog目录操作
from markdown.extensions.toc import TocExtension
# 字体操作
from django.utils.text import slugify


# def index(request):
#     return HttpResponse('欢迎访问我的博客首页')


def index(request):
    post_list = Article.objects.all()
    print(post_list)
    return render(request, 'blog/index.html', context={"post_list": post_list
                                                       })


def archive(request, year, month):
    post_list = Article.objects.filter(created_time__year=year,
                                       created_time__month=month
                                       ).order_by('-created_time')
    return render(request, 'blog/index.html', context={"post_list": post_list
                                                       })

# 分类
def category(request, pk):
    # 记得在开始部分导入 Category 类
    cate = get_object_or_404(Category, pk=pk)
    post_list = Article.objects.filter(category=cate).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})

# 标签
def tag(request, pk):
    # 记得在开始部分导入 Category 类
    t = get_object_or_404(Tag, pk=pk)
    post_list = Article.objects.filter(tags=t).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})


# def category(request, pk):
#     cate = get_object_or_404(Category, pk=pk)
#     post_list = Category.objects.filter(
#         id=cate).order_by('-created_time')
#     return render(request, 'blog/index.html', context={"post_list": post_list
#                                                        })


def detail(request, pk):
    # detail 视图中解析markdown
    # 在markdown文章中加[TOC]可以在文章内容生成目录
    post = get_object_or_404(Article, pk=pk)
    # init 支持markdown
    # post.body = markdown.markdown(
    #     post.body, extensions=[
    #         'markdown.extensions.extra', 'markdown.extensions.codehilite', 'markdown.extensions.toc', ])
    # 在页面的任何地方插入目录 生成侧边目录
    md = markdown.Markdown(
        extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
            # 秒点url用标题
            TocExtension(slugify=slugify),
        ])
    post.body = md.convert(post.body)
    # post.toc = md.toc
    # 处理空目录 文章没有标题 右边目录不会异常
    m = re.search(r'<div class="toc">\s*<ul>(.*)</ul>\s*</div>', md.toc, re.S)
    post.toc = m.group(1) if m is not None else ''
    return render(request, 'blog/detail.html', context={'post': post})
