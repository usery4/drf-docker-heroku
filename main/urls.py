from django.urls import path , include
from .views import ArticleViewSet
from rest_framework.routers import DefaultRouter
from main import views


router = DefaultRouter()
router.register('article', ArticleViewSet, basename='article')

urlpatterns = [

    path('', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls) ),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]
