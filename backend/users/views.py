from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.models import User

from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, permission_classes=((IsAuthenticated,)))
    def me(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)
