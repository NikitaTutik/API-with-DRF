from rest_framework import generics
from .serializers import PostSerializer
from .models import Post

class PostListCreateView(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
