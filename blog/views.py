from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
# views.py
from rest_framework import viewsets
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework.response import Response
from rest_framework.decorators import action

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # Комментарий қосу үшін арнайы action жасау
    @action(detail=True, methods=['post'])
    def add_comment(self, request, pk=None):
        post = self.get_object()  # Постты табу
        serializer = CommentSerializer(data=request.data)  # Комментарий сериализациясы
        if serializer.is_valid():  # Егер сұрау дұрыс болса
            serializer.save(post=post)  # Комментарийді сақтау
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
