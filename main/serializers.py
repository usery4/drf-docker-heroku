from rest_framework import serializers
from .models import Article
from django.contrib.auth.models import User



class UserSerializer(serializers.HyperlinkedModelSerializer):
    articles = serializers.HyperlinkedRelatedField(many=True, view_name='article-detail', read_only=True)
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = User
        fields = ['id','owner', 'username', 'articles', 'url']


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')


    class Meta:
        model = Article
        fields = '__all__'

