from rest_framework.permissions import IsAuthenticated
from utils.permission import IsOwnerOrReadOnly
from rest_framework import mixins
from rest_framework import viewsets
from .models import Comment
from django.shortcuts import render

# Create your views here.


class CommentSet(mixins.CreateModelMixin,  mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Comment.objects.all()
    # permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
