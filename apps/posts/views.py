from .models import Software
from .models import SoftwareDetail
from .models import Programming
from .models import ProgrammingDetail
from .serializers import SoftwareSerializer
from .serializers import SoftwareDetailSerializer

# one way to come true
# from rest_framework.views import APIView
# from rest_framework.response import Response
#
# class Software_list(APIView):
#     """
#     List all snippets, or create a new snippet.
#     """
#     def get(self, request, format=None):
#         Softwares = Software.objects.all()
#         serializer = SoftwareSerializer(Softwares, many=True)
#         return Response(serializer.data)
# ------------------------------------------------------------------------------
# the other way
from rest_framework.pagination import PageNumberPagination
from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets



# set pagination
class SoftwaresPagination(PageNumberPagination):
    page_size = 10,
    page_size_query_param = 'page_size'
    page_query_param = "p"
    max_page_size = 100


class SoftwareListSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = SoftwareSerializer
    pagniation_class = SoftwaresPagination
    # 手动实现过滤
    def get_queryset(self):
        queryset = Software.objects.all()
        software_type = self.request.query_params.get("type", "")
        if software_type != "All":
            queryset = queryset.filter(type=software_type)
        return queryset


class SoftwareDetailSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = SoftwareDetailSerializer

    def get_queryset(self):
        queryset = SoftwareDetail.objects.all()
        software_id = self.request.query_params.get("id", 0)
        if software_id:
            queryset = queryset.filter(id=software_id)
        return queryset


class ProgramListSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = SoftwareSerializer
    # 手动实现过滤
    def get_queryset(self):
        queryset = Programming.objects.all()
        programming_type = self.request.query_params.get("type", "")
        if programming_type != "All":
            queryset = queryset.filter(type=programming_type)
        return queryset


class ProgramDetailSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = SoftwareDetailSerializer

    def get_queryset(self):
        queryset = SoftwareDetail.objects.all()
        software_id = self.request.query_params.get("id", 0)
        if software_id:
            queryset = queryset.filter(id=software_id)
        return queryset
