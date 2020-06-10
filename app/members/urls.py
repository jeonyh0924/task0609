from django.urls import path
from rest_framework.routers import DefaultRouter

from members import views
from members.views import AuthTokenAPIView, CustomAuthToken

router = DefaultRouter()
router.register('users', views.UserModelViewSetAPI)
router.register('card', views.CardModelViewSetAPI)
urlpatterns_members = [
    path('token/', AuthTokenAPIView.as_view()),
    path('login/', CustomAuthToken.as_view()),
]

urlpatterns_members += router.urls
