from django.urls import path, re_path, include
import xadmin
from posts.views import SoftwareViewset
from posts.views import ProgramViewset
from posts.views import OpensourceViewset
from users.views import UserViewset
from posts.views import ExperienceViweset
from posts.views import QuestionViweset
from posts.views import HomeViewset
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views
from django.contrib import admin

router = DefaultRouter()
router.register(r'softwares', SoftwareViewset, base_name="softwares")
router.register(r'program', ProgramViewset, base_name="program")
router.register(r'opensource', OpensourceViewset, base_name="opensource")
router.register(r'register', UserViewset, base_name="register")
router.register(r'experience', ExperienceViweset, base_name="experience")
router.register(r'question', QuestionViweset, base_name="question")
router.register(r'home', HomeViewset, base_name="home")

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('^', include(router.urls)),
    re_path('^api-auth/', include('rest_framework.urls', namespace="rest_framework")),
    re_path('^docs/', include_docs_urls(title="GeekBay")),
    # drf 自带token认证模式
    # re_path('^login/', views.obtain_auth_token),
    re_path('^login', obtain_jwt_token),
    re_path('mdeditor/', include('mdeditor.urls')),
]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
