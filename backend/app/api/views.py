from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Todo
from .serializers import TodoSerializer

class TodoViewSet(viewsets.ModelViewSet):
    #permission_classes = (IsAuthenticated, )
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    #def get_queryset(self):
    #    return Todo.objects.get(user=self.request.user)