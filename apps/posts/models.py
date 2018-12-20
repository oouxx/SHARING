from datetime import datetime
from mdeditor.fields import MDTextField
from django.contrib.auth import get_user_model
from django.db import models
User = get_user_model()


class Post(models.Model):
    id = models.BigIntegerField(primary_key=True)
    title = models.CharField(max_length=20, verbose_name="标题", default="")
    # 规定注册了的用户才能投稿
    contribute_person = models.ForeignKey(User, verbose_name="发布者", null=True, blank=True,
                                          on_delete=models.SET_NULL)
    release_time = models.DateTimeField(default=datetime.now, verbose_name="发布时间")
    modify_time = models.DateTimeField(default=datetime.now, verbose_name="最新修改时间")
    comment_no = models.IntegerField(verbose_name="评论数", null=True, blank=True)
    like_no = models.IntegerField(verbose_name="点赞数", null=True, blank=True)
    isHot = models.BooleanField(default=False, verbose_name="是否热搜")
    slug = models.SlugField(verbose_name="子模型名", max_length=100, default="")

    class Meta:
        ordering = ['modify_time']


class Software(Post):
    """
    软件
    """
    category = (
        ("All", "All"),
        ("Windows", "Windows"),
        ("Android", "Android"),
        ("IOS", "IOS"),
        ("MAC", "MAC"),
        ("Linux", "Linux")
    )
    type = models.CharField(choices=category, verbose_name="软件分类", max_length=10, default="All")
    icon = models.ImageField(max_length=100, upload_to="media/software/icon/%Y/%m", verbose_name="软件icon", default="/media/default_avatar.jpeg", null=True, blank=True)
    description = MDTextField(verbose_name="软件描述")



    class Meta:
        verbose_name = "软件"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Opensource(Post):
    """
    开源
    """
    categories = (
        ("", ""),
        ("typeOne", "typeOne"),
        ("typeTwo",  "typeTwo")
    )
    type = models.CharField(max_length=10, verbose_name="分类", choices=categories, default="")
    description = MDTextField(verbose_name="描述")
    cover = models.ImageField(max_length=100, upload_to="media/opensource/cover/%Y/%m", verbose_name="封面", null=True, blank=True)

    class Meta:
        verbose_name = "开源"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Programming(Post):
    """
    编程
    """
    category = (
        ("", ""),
        ("Java", "Java"),
        ("Python", "Python"),
        ("C", "C"),
        ("C++", "C++"),
        ("Ruby", "Ruby"),
        ("Go", "Go"),
        ("JavaScript", "JavaScript")
    )
    type = models.CharField(choices=category, verbose_name="编程语言", max_length=10, default="")
    description = MDTextField(verbose_name="软件描述")
    cover = models.ImageField(max_length=100, upload_to="media/programming/cover/%Y/%m", verbose_name="封面", null=True, blank=True)

    class Meta:
        verbose_name = "编程"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Experience(Post):
    """
    经验分享
    """
    description = MDTextField(verbose_name="详情")

    class Meta:
        verbose_name = "经验"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Question(Post):
    """
    提问
    """
    description = MDTextField(verbose_name="详情")

    class Meta:
        verbose_name = "问答"
        verbose_name_plural= verbose_name

    def __str__(self):
        return self.title

