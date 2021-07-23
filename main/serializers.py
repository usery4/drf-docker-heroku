from rest_framework import serializers
from .models import Article
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    main = serializers.PrimaryKeyRelatedField(many=True, queryset=Article.objects.all())

    class Meta:
        model = User
        fields = [ 'username']

class ArticleSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Article
        fields = '__all__'

