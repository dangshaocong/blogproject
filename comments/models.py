from django.db import models
from django.utils import timezone

# Create your models here.


class Comment(models.Model):
    # 用户名 邮箱 个人网址(可选) 内容 创建时间(提交时间) 属于的文章(外键到文章表)
    name = models.CharField('名字', max_length=50)
    email = models.EmailField('邮箱')
    url = models.URLField('网址', blank=True)
    text = models.TextField('内容')
    created_time = models.DateTimeField('创建时间', default=timezone.now)
    post = models.ForeignKey(
        'blog.Article',
        verbose_name='文章',
        on_delete=models.CASCADE)

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{}: {}'.format(self.name, self.text[:20])
