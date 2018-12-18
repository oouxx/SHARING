from .models import Software
from .models import Programming
from .models import Opensource
from .models import Experience
from .models import Question
from .serializers import SoftwareSerializer
from .serializers import ProgramSerializer
from .serializers import OpensourceSerializer
from .serializers import ExperienceSerializer
from .serializers import HomeSerializer
from .serializers import QuestionSerializer
from rest_framework import permissions
from rest_framework.pagination import PageNumberPagination
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response


class SoftwaresPagination(PageNumberPagination):
    page_size = 10,
    page_size_query_param = 'page_size'
    page_query_param = "p"
    max_page_size = 100


class SoftwareViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = SoftwareSerializer
    queryset = Software.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('type', )


class ProgramViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = ProgramSerializer
    queryset = Programming.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('type', )


class OpensourceViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = OpensourceSerializer
    queryset = Opensource.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('type', )


class ExperienceViweset(viewsets.ModelViewSet):
    """
    get:
        获取经验
    create:
        创建经验
    destroy:
        删除经验
    update:
        修改经验
    """
    serializer_class = ExperienceSerializer
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    queryset = Experience.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id', )

    def get_permissions(self):
        if self.action == "create":
            return [permissions.IsAuthenticated()]
        elif self.action == "retrieve":
            return []
        return []


class QuestionViweset(viewsets.ModelViewSet):
    """
    get:
        获取最近的提问
    create:
        发出问答
    destroy:
        删除问答
    update:
        修改问答
    """
    serializer_class = QuestionSerializer
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    queryset = Question.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id', )

    def get_permissions(self):
        if self.action == "create":
            return [permissions.IsAuthenticated()]
        elif self.action == "retrieve":
            return []
        return []

class HomeViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    get:
        获取首页内容
    """
    serializer_class = HomeSerializer

    def get_queryset(self):
        from itertools import chain
        sowa = Software.objects.filter()
        opso = Opensource.objects.filter()
        expe = Experience.objects.filter()
        prog = Programming.objects.filter()
        queryset = sorted(
            chain(sowa, opso, expe, prog),
            key=lambda car: car.modify_time, reverse=True)
        return queryset
