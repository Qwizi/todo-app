from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


from .serializers import UserSerializer
from api.serializers import TodoSerializer
from api.models import Todo

class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, permission_classes=((IsAuthenticated,)))
    def me(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)

    @action(detail=False, permission_classes=((IsAuthenticated,)))
    def todos(self, request):
        user = request.user
        queryset = Todo.objects.filter(user=user)
        serializer = TodoSerializer(queryset, many=True)
        return Response(serializer.data)
