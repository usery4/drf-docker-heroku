import django_filters
from .models import Article
from .serializers import ArticleSerializer, UserSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from main.serializers import UserSerializer
from rest_framework import permissions, generics
from main.permissions import IsOwnerOrReadOnly
from rest_framework import filters
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework.response import Response



class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['owner', 'author']
    search_fields = ['title', ]


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes =[permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['id', 'username']
    search_fields = ['username']

class ArticleHighlight(generics.GenericAPIView):
    queryset = Article.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer]

    def get(self, request, *args, **kwargs):
        article = self.get_object()
        return Response(article.highlighted)