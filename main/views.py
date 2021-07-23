import django_filters

from .models import Article
from .serializers import ArticleSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from main.serializers import UserSerializer
from rest_framework import permissions, generics
from main.permissions import IsOwnerOrReadOnly
from rest_framework import filters
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend





class ArticleFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Article
        fields = ('title',)

class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['owner', 'author']
    search_fields = ['title', ]


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

