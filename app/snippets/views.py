from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer

User = get_user_model()


class SnippetFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')

    startswich_title = filters.CharFilter(field_name='title', method='filter_startswitch_title')

    def filter_startswitch_title(self, queryset, name, value):
        title_filter = {f'{name}__startswith': value}
        return queryset.filter(**title_filter)

    class Meta:
        model = Snippet
        fields = ['min_price', 'max_price', 'startswich_title', ]


class SnippetViewSet(viewsets.ModelViewSet):
    authentication_classes = [
        TokenAuthentication,
    ]
    permission_classes = [
        IsAuthenticated,
    ]

    filter_backends = [filters.DjangoFilterBackend, ]
    filterset_class = SnippetFilter

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    # filter_backends = [filters.SearchFilter]
    # search_fields = ['title', 'code', ]

    # def list(self, request, *args, **kwargs):
    #     print(request.user.username)
    #     return super().list(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_permissions(self):
        permission_classes = [IsAuthenticated(), ]
        return permission_classes
