from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class UserProfile(AbstractUser):
    """
    用户
    """
    mobile = models.CharField(max_length=11, null=True, blank=True, unique=True, verbose_name="电话",)
    birth = models.DateField(null=True, blank=True, verbose_name="生日")
    head = models.ImageField(max_length=100, upload_to="media/head", default="/default_head.jpg", verbose_name="头像")
    email = models.EmailField(max_length=100, verbose_name="邮箱")
    per_sign = models.CharField(max_length=100, verbose_name= "个性签名")

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name
    def __unicode__(self):
      return self.username


class VerifyCode(models.Model):
    """
    短信验证码
    """
    code = models.CharField(max_length=10, verbose_name="验证码")
    mobile = models.CharField(max_length=11, verbose_name="电话")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "短信验证码"
        verbose_name_plural = verbose_name
        app_label = "users"

    def __str__(self):
        return self.code