from django.contrib.auth import get_user_model, authenticate

# Create your views here.
from rest_framework import generics, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import action
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from members.models import Card
from members.permissions import IsOwnerOrReadOnly, CardPermission
from members.serializers import UserSerializer, CardSerializer

User = get_user_model()


class UserModelViewSetAPI(viewsets.ModelViewSet):
    authentication_classes = [
        TokenAuthentication,
    ]
    permission_classes = [
        IsAuthenticated,
        IsOwnerOrReadOnly,
    ]
    ordering = ['-pk', ]

    queryset = User.objects.all()
    serializer_class = UserSerializer

    # @action(detail=True, methods=['POST', ])
    # def addCard(self, request, pk=None):
    #     card = Card.objects.get(pk=pk)
    #     user = request.user
    #


class CardModelViewSetAPI(viewsets.ModelViewSet):
    authentication_classes = [
        TokenAuthentication,
    ]
    permission_classes = [
        IsAuthenticated,
        CardPermission,
    ]
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    def perform_create(self, serializer):
        # 토큰인증을 하지 않아도 요청을 보내면 카드를 만들 수 있어요 !
        user = User.objects.first()
        serializer.save(
            # user=self.request.user
            # user=user
        )


class AuthTokenAPIView(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        user = authenticate(username=username, password=password)

        if user:
            token, _ = Token.objects.get_or_create(user=user)
        else:
            raise AuthenticationFailed()

        data = {
            'token': token.key,
            'user': UserSerializer(user).data,
        }
        return Response(data)


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })
