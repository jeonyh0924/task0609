from django.urls import path, include
from rest_framework.routers import DefaultRouter

from snippets import views
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)

urlpatterns = [
    # path('snippets/', views.snippet_list),
    # path('snippets/<int:pk>/', views.snippet_detail),
    path('', include(router.urls)),
]