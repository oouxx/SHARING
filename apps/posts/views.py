from .models import Software
from .serializers import SoftwareSerializer


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
from django_filters.rest_framework import DjangoFilterBackend
from .filter import SoftwaresFilter
from rest_framework.authentication import TokenAuthentication


# set pagination
class SoftwaresPagination(PageNumberPagination):
    page_size = 10,
    page_size_query_param = 'page_size'
    page_query_param = "p"
    max_page_size = 100


class SoftwareListSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Software.objects.all()
    serializer_class = SoftwareSerializer
    pagniation_class = SoftwaresPagination
    filter_class = SoftwaresFilter
    # authentication_classes = (TokenAuthentication,)






    # filter_backends = (DjangoFilterBackend, )   #   元祖后面要加“，”，  坑啊，以前不重视
    # filter_field = ("type" ,"comment_no" ,"like_no")

    # 手动实现过滤
    # def get_queryset(self):
    #     queryset = Software.objects.all()
    #     software_type = self.request.query_params.get("type", "")
    #     if type:
    #         queryset = queryset.filter(type=software_type)
    #     return queryset

