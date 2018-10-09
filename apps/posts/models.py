from datetime import datetime

from django.db import models
from users.models import UserProfile
# Create your models here.


class Software(models.Model):
    """
    软件
    """
    category = (
        (1, "Windows"),
        (2, "Android"),
        (3, "IOS"),
        (4, "MAC"),
        (5, "Linux"),
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
    comment_no = models.IntegerField(verbose_name="评论数")
    like_no = models.IntegerField(verbose_name="点赞数")

    #资源本身的属性
    icon = models.ImageField(max_length=100, upload_to="media/software/icon/%Y/%m", verbose_name="软件icon")
    type = models.IntegerField(choices=category, verbose_name="软件分类")
    description = models.TextField(verbose_name="软件描述")

    class Meta:
        verbose_name = "软件"
        verbose_name_plural = verbose_name

    def  str__(self):
        return self.title

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

    # 资源本身的属性
    project_addr = models.CharField(max_length=100, verbose_name="项目地址")
    description = models.TextField(verbose_name="软件描述")
    class Meta:
        verbose_name = "开源"
        verbose_name_plural = verbose_name
    def  __str__(self):
        return self.title

class Hacker(models.Model):
    pass
class Programming(models.Model):
    """
    编程
    """
    category = (
        (1, "Java"),
        (2, "Python"),
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

    # 资源本身的属性
    type = models.IntegerField(choices=category, verbose_name="编程语言")
    description = models.TextField(verbose_name="软件描述")

    class Meta:
        verbose_name = "编程语言"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.title