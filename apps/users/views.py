# Create your views here.
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from random import choice
from rest_framework import permissions
from rest_framework import authentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from rest_framework_jwt.serializers import jwt_encode_handler, jwt_payload_handler

# from .serializers import SmsSerializer, UserRegSerializer, UserDetailSerializer
from GeekBay.settings import APIKEY
from utils.yunpian import YunPian
from .models import VerifyCode

User = get_user_model()


class CustomBackend(ModelBackend):
    """
    自定义用户验证
    """
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username)|Q(mobile=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None

# class Login(View):
#
#     def get(self, request):
#         return render(request, "login.html")
#     def post(self, request):
#         try:
#             from django.contrib.auth import authenticate, login
#             self.user_name = request.POST.get("username", "")
#             self.pass_word = request.POST.get("password", "")
#             user = authenticate(username=self.user_name, password= self.pass_word)
#             if user is not None:
#                 login(request, user)
#                 return render(request, "login_success.html", {})
#         except:
#             print("login failed")
#             return render(request, "index.html", {})
