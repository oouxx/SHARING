from datetime import datetime
from mdeditor.fields import MDTextField
from django.db import models
from users.models import UserProfile
# Create your models here.


class Software(models.Model):
    """
    软件
    """
    category = (
        ("", ""),
        ("Windows", "Windows"),
        ("Android", "Android"),
        ("IOS", "IOS"),
        ("MAC", "MAC"),
        ("Linux", "Linux")
    )
    # 帖子本身的属性
    title = models.CharField(max_length=20, verbose_name="标题", default="")
    release_person = models.ForeignKey(UserProfile, verbose_name="帖子发布者", null=True, blank=True,
                                       on_delete=models.SET_NULL, related_name="release_person")
    # 规定注册了的用户才能投稿
    contribute_person = models.ForeignKey(UserProfile, verbose_name="帖子投稿者", null=True, blank=True,
                                          on_delete=models.SET_NULL, related_name="contribute_person")
    release_time = models.DateTimeField(default=datetime.now, verbose_name="发布时间")
    modify_time = models.DateTimeField(default=datetime.now, verbose_name="最新修改时间")
    comment_no = models.IntegerField(verbose_name="评论数", null=True, blank=True)
    like_no = models.IntegerField(verbose_name="点赞数", null=True, blank=True)
    type = models.CharField(choices=category, verbose_name="软件分类", max_length=10, default="")

    class Meta:
        verbose_name = "软件"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class SoftwareDetail(models.Model):

    # 资源本身的属性
    # 标题之间是一对一的关系,related_name 的作用是可以通过software.title来
    software = models.OneToOneField(Software, verbose_name="标题", related_name= "detail", on_delete=models.CASCADE)
    icon = models.ImageField(max_length=100, upload_to="media/software/icon/%Y/%m", verbose_name="软件icon")
    description = MDTextField(verbose_name="软件描述")

    class Meta:
        verbose_name = "软件详情"
        verbose_name_plural = verbose_name

    def __str__(self):
        # 返回标题
        return self.software.title


class Opensource(models.Model):
    """
    开源
    """

    # 帖子本身的属性
    title = models.CharField(max_length=20, verbose_name="标题", default="")
    release_person = models.ForeignKey(UserProfile, verbose_name="帖子发布者", null=True, blank=True,
                                       on_delete=models.SET_NULL, related_name="+")
    # 规定注册了的用户才能投稿
    contribute_person = models.ForeignKey(UserProfile, verbose_name="帖子投稿者", null=True, blank=True,
                                          on_delete=models.SET_NULL, related_name="+")
    release_time = models.DateTimeField(default=datetime.now, verbose_name="发布时间")
    modify_time = models.DateTimeField(default=datetime.now, verbose_name="最新修改时间")
    comment_no = models.IntegerField(verbose_name="评论数")
    like_no = models.IntegerField(verbose_name="点赞数")

    class Meta:
        verbose_name = "开源"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class OpensourceDetail(models.Model):

    # 资源本身的属性
    opensource = models.ForeignKey(Opensource, on_delete=models.CASCADE, related_name="detail")
    project_addr = models.CharField(max_length=100, verbose_name="项目地址")
    description = MDTextField(verbose_name="软件描述")

    class Meta:
        verbose_name = "开源项目详情"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.opensource.title


class Programming(models.Model):
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
    # 帖子本身的属性
    title = models.CharField(max_length=20, verbose_name="标题", default="")
    release_person = models.ForeignKey(UserProfile, verbose_name="帖子发布者", null=True, blank=True,
                                       on_delete=models.SET_NULL, related_name="+")
    # 规定注册了的用户才能投稿
    contribute_person = models.ForeignKey(UserProfile, verbose_name="帖子投稿者", null=True, blank=True,
                                          on_delete=models.SET_NULL, related_name="+")
    release_time = models.DateTimeField(default=datetime.now, verbose_name="发布时间")
    modify_time = models.DateTimeField(default=datetime.now, verbose_name="最新修改时间")
    comment_no = models.IntegerField(null=True, blank=True, verbose_name="评论数")
    like_no = models.IntegerField(null=True, blank=True, verbose_name="点赞数")
    type = models.CharField(choices=category, verbose_name="编程语言", max_length=10, default="")

    class Meta:
        verbose_name = "编程语言"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class ProgrammingDetail(models.Model):
    category = (
        (1, "Java"),
        (2, "Python"),
    )
    programming = models.ForeignKey(Programming, on_delete=models.CASCADE, related_name="detail")
    # 资源本身的属性
    type = models.IntegerField(choices=category, verbose_name="编程语言")
    description = MDTextField(verbose_name="软件描述")

    class Meta:
        verbose_name = "编程详情"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.programming.title
