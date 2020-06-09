from django.shortcuts import render

# Create your views here.
from rest_framework import permissions, viewsets

from snippets.models import Snippet
# from snippets.permissions import IsOwnerOrReadOnly
from snippets.serializers import SnippetSerializer


class SnippetViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [
        # permissions.IsAuthenticatedOrReadOnly,
                          # IsOwnerOrReadOnly,
                          ]
