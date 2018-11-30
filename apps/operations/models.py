from datetime import datetime
from users.models import UserProfile
from django.db import models
from posts.models import Opensource, Software, Programming
# Create your models here.

class Explore(models.Model):
    """
    用户探讨区
    """
    user = models.ForeignKey(UserProfile, on_delete = models.CASCADE, verbose_name= "用户")
    time = models.DateTimeField(default= datetime.now, verbose_name="发起时间")
    content = models.TextField(verbose_name="探讨内容")

    class Meta:
        verbose_name = "用户探讨"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user





class Comment(models.Model):
    """
    用户评论
    """

    user = models.ForeignKey(UserProfile, on_delete = models.CASCADE, related_name= "+", verbose_name= "用户")
    time = models.DateTimeField(default= datetime.now, verbose_name="评论时间")
    content = models.TextField(verbose_name= "评论的内容")
    comm2opensource = models.ForeignKey(Opensource, verbose_name= "评论开源", on_delete=models.CASCADE, default="")
    comm2software = models.ForeignKey(Software, verbose_name="评论软件", on_delete=models.CASCADE, default="")
    comm2programming = models.ForeignKey(Programming, verbose_name="评论编程", on_delete=models.CASCADE, default="")
    comm2Explore = models.ForeignKey(Explore,verbose_name="评论探讨", on_delete=models.CASCADE, default="")
    class Meta:
        verbose_name = "用户评论"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user





