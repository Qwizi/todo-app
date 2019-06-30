from rest_framework import (
    viewsets,
    status
)
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import (
    get_object_or_404, 
    get_list_or_404
)

from .serializers import TodoSerializer
from .models import Todo

class TodoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = TodoSerializer

    def get_queryset(self):
        return get_list_or_404(Todo, user=self.request.user)

    def get_object(self):
        return get_object_or_404(Todo, id=self.kwargs['pk'], user=self.request.user)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
