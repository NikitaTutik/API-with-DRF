from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PostSerializer
from .models import Post
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework import mixins


class PostListCreateView(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
