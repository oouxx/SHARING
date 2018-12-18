from datetime import datetime
from mdeditor.fields import MDTextField
from django.db import models
from users.models import UserProfile


class CommonFields(models.Model):
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


class Software(CommonFields):
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
    type = models.CharField(choices=category, verbose_name="软件分类", max_length=10, default="")
    icon = models.ImageField(max_length=100, upload_to="media/software/icon/%Y/%m", verbose_name="软件icon")
    description = MDTextField(verbose_name="软件描述")

    class Meta:
        verbose_name = "软件"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Opensource(CommonFields):
    """
    开源
    """
    categories = (
        ("", ""),
        ("typeOne", "typeOne"),
        ("typeTwo",  "typeTwo")
    )
    type = models.CharField(max_length=10, verbose_name="分类", choices=categories, default="")
    description = MDTextField(verbose_name="软件描述")

    class Meta:
        verbose_name = "开源"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Programming(CommonFields):
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

    class Meta:
        verbose_name = "编程语言"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Experience(models.Model):
    """
    经验分享
    """
    user = models.ForeignKey(UserProfile, verbose_name="经验分享者", on_delete=models.CASCADE, related_name="experience")
    title = models.CharField(max_length=20, verbose_name="标题", default="")
    release_time = models.DateTimeField(default=datetime.now, verbose_name="发布时间")
    modify_time = models.DateTimeField(default=datetime.now, verbose_name="最新修改时间")
    description = MDTextField(verbose_name="详情")
    icon = models.ImageField(max_length=100, upload_to="media/experience/icon/%Y/%m", verbose_name="封面")

    class Meta:
        verbose_name = "经验"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Post(models.Model):
    software = models.ForeignKey(Software, on_delete=models.CASCADE, verbose_name="软件")
    opensource = models.ForeignKey(Opensource, on_delete=models.CASCADE, verbose_name="开源")
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE, verbose_name="经验")
    Programming = models.ForeignKey(Programming, on_delete=models.CASCADE, verbose_name="编程")

    class Meta:
        verbose_name = "POST"
        verbose_name_plural = verbose_name
