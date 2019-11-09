from django.contrib import admin
from .models import Article, Category, Tag

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'created_time',
        'modified_time',
        'category',
        'author']
    fields = ['title', 'body', 'excerpt', 'category', 'tags']

    # 将后台登录的用户保存到数据库
    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)
    # 文章创建时间和修改时间也需要自动保存


admin.site.register(Article, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
