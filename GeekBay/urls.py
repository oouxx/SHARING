"""GeekBay URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path, re_path, include
import xadmin
from django.views.generic import TemplateView
from users.views import Login
from posts.views import SoftwareListSet
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views





router = DefaultRouter()
# set softwares' url
router.register(r'softwares', SoftwareListSet, base_name="softwares")


urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    re_path('^', include(router.urls)),
    path('', TemplateView.as_view(template_name="index.html"), name="index"),
    re_path('^api-auth/', include('rest_framework.urls', namespace="rest_framework")),
    re_path('^login/$', Login.as_view(), name= "login"),
    re_path('^docs/', include_docs_urls(title="GeekBay")),
    re_path('^api-token-auth/', views.obtain_auth_token)

]
