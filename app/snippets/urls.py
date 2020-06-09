from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from snippets.views import UserViewSet, AuthTokenAPIView
from snippets import views

# router = DefaultRouter()
# router.register(r'snippets', views.SnippetViewSet)


router = routers.SimpleRouter()
router.register(r'snippets', views.SnippetViewSet, basename='snippet')
router.register('users', UserViewSet, basename='user')

urlpatterns =[
    path('', include(router.urls)),
    path('auth/', AuthTokenAPIView.as_view()),
    # path('users/', views.UserList.as_view()),
    # path('users/<int:pk>/', views.UserDetail.as_view()),
]
