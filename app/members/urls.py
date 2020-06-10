from django.urls import path
from rest_framework.routers import DefaultRouter

from members import views
from members.views import AuthTokenAPIView

router = DefaultRouter()
router.register('', views.UserModelViewSet)

urlpatterns_members = [
    path('token/', AuthTokenAPIView.as_view()),
]

urlpatterns_members += router.urls
