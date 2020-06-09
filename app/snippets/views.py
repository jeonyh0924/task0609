from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import permissions, viewsets, generics, status
from django.contrib.auth.models import User
from rest_framework.pagination import CursorPagination
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer, UserSerializer
from rest_framework import filters


class SnippetViewSet(viewsets.ModelViewSet):
    """
#     This viewset automatically provides `list`, `create`, `retrieve`,
#     `update` and `destroy` actions.
#
#     Additionally we also provide an extra `highlight` action.
#     """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        # IsOwnerOrReadOnly,
    ]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'code', ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

#
# class SnippetViewSet(viewsets.ViewSet):
#     filter_backends = [filters.SearchFilter]
#     search_fields = ['title', 'code', ]
#
#     def get_object(self, pk):
#         try:
#             return Snippet.objects.get(pk=pk)
#         except Snippet.DoesNotExist:
#             raise Http404
#
#     def list(self, request):
#         queryset = Snippet.objects.all()
#         serializer = SnippetSerializer(queryset, many=True)
#         return Response(serializer.data)
#
#     def create(self, request):
#         serializer = SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUESTd)
#
#     def retrieve(self, request, pk=None):
#         queryset = Snippet.objects.all()
#         snippet = get_object_or_404(queryset, pk=pk)
#         serializer = SnippetSerializer(snippet)
#         return Response(serializer.data)
#
#     def update(self, request, pk, format=None):
#         queryset = self.get_object(pk)
#         serializer = SnippetSerializer(queryset, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def destroy(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         snippet.delete()
#         data = {
#             'message': f"{snippet} 해당 스니펫은 삭제가 되었습니다."
#         }
#         return Response(data, status=status.HTTP_204_NO_CONTENT)


# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#
# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
class UserViewSet(viewsets.ViewSet):


    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        queryset = User.objects.all()
        user = User.get_object_or_404(queryset, pk=pk)
        user.delete()
        return Response(status.HTTP_204_NO_CONTENT)


class AuthTokenAPIView(APIView):
    def get(self, request):
        pass

    def post(self, request):
        pass