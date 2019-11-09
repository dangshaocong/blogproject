from django import template

from ..models import Article, Category, Tag

register = template.Library()

# 最新文章标签 5个
@register.inclusion_tag('blog/inclusions/_recent_posts.html', takes_context=True)
def show_recent_posts(context, num=5):
    return {
        'recent_post_list': Article.objects.all().order_by('-created_time')[:num],
    }

# 归档模板标签 按月归档
@register.inclusion_tag('blog/inclusions/_archives.html', takes_context=True)
def show_archives(context):
    return {
        'date_list': Article.objects.dates('created_time','month',order='DESC'),
    }

# 文章归类模板标签
@register.inclusion_tag('blog/inclusions/_categories.html', takes_context=True)
def show_categories(context):
    return {
        'category_list': Category.objects.all(),
    }

# 文章标签云模板标签
@register.inclusion_tag('blog/inclusions/_tags.html', takes_context=True)
def show_tags(context):
    return {
        'tag_list': Tag.objects.all(),
    }
