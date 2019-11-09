from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


# Create your models here.
# 分类 种类
# 需要建立至少3 个表 文章 分类 标签

class Category(models.Model):
    # 分类
    """
     django 要求模型必须继承 models.Model 类。
     这个是blog的分类 只需要定义一个name就好 id 会默认生成
     CharField 定义了 name的数据类型
     其中 charfiled是字符型 其实还有日期
     DateTimeField、整数类型 IntegerField 等等

    """
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Tag(models.Model):
    # 标签 这里也只要定义标签name就好
    """
     django 要求模型必须继承 models.Model 类。
     这个是blog的分类 只需要定义一个name就好 id 会默认生成
     CharField 定义了 name的数据类型
     其中 charfiled是字符型 其实还有日期
     DateTimeField、整数类型 IntegerField 等等

    """
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Article(models.Model):
    # 文章 有 标题 正文内容 发布时间 分类 标签 作者
    """
     django 要求模型必须继承 models.Model 类。
     这个是blog的分类 只需要定义一个name就好 id 会默认生成
     CharField 定义了 name的数据类型
     其中 charfiled是字符型 其实还有日期
     DateTimeField、整数类型 IntegerField 等等

    """
    # 标题
    title = models.CharField('标题', max_length=70)
    # 正文
    body = models.TextField('正文')
    # 创建时间和最后一次修改时间
    created_time = models.DateTimeField('创建时间', default=timezone.now)
    modified_time = models.DateTimeField('修改时间')
    # 摘要 默认可以为空
    excerpt = models.CharField('摘要', max_length=200, blank=True)
    # 分类 是 1对多的关系也就是说 1篇文章只能有一个分类 但是一个分类下面可以有多个文章 用外键关联
    # on_delete 表示当关联的数据被删除时，被关联的数据的行为
    category = models.ForeignKey(
        Category,
        verbose_name='分类',
        on_delete=models.CASCADE)
    # 对于标签 1篇文章可以用多个标签 1个标签也可以有多个文章 多对多 标签可以为空
    tags = models.ManyToManyField(Tag, verbose_name='标签', blank=True)
    # 作者
    # 文章作者，这里 User 是从 django.contrib.auth.models 导入的。
    author = models.ForeignKey(
        User,
        verbose_name='作者',
        on_delete=models.CASCADE)

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
    # 文章更新时间

    def save(self, *args, **kwargs):
        self.modified_time = timezone.now()
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

