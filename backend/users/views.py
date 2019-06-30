from rest_framework import (
    viewsets,
    status
)
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from .serializers import (
    UserSerializer,
    UsernameSerializer,
    PasswordSerializer,
    EmailSerializer
)
from todos.serializers import TodoSerializer
from todos.models import Todo

class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, permission_classes=((IsAuthenticated,)))
    def me(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)

    @action(detail=False, permission_classes=((IsAuthenticated,)), methods=['put'])
    def change_username(self, request):
        user = request.user
        serializer = UsernameSerializer(data=request.data)
        if serializer.is_valid():
            user.username = serializer.data['username']
            user.save()
            return Response({'status': 'Username changed'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, permission_classes=((IsAuthenticated,)), methods=['put'])
    def change_password(self, request):
        user = request.user
        serializer = PasswordSerializer(data=request.data)
        if serializer.is_valid():
            user.set_password(serializer.data['password'])
            user.save()
            return Response({'status': 'Password changed'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, permission_classes=((IsAuthenticated,)), methods=['put'])
    def change_email(self, request):
        user = request.user
        serializer = EmailSerializer(data=request.data)
        if serializer.is_valid():
            user.email = serializer.data['email']
            user.save()
            return Response({'status': 'E-mail changed'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

