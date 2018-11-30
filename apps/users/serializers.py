# -*- coding: utf-8 -*-
__author__ = 'bobby'
import re
from rest_framework import serializers
from django.contrib.auth import get_user_model
from datetime import datetime
from datetime import timedelta
from rest_framework.validators import UniqueValidator

from .models import VerifyCode

from GeekBay.settings import REGEX_MOBILE

User = get_user_model()


class UserDetailSerializer(serializers.ModelSerializer):
    """
    用户详情序列化类
    """

    class Meta:
        model = User
        fields = ("name", "gender", "birthday", "email", "mobile")

