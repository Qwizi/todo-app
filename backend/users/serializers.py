from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'username',
            'password'
        )
        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class UsernameSerializer(serializers.Serializer):
    username = serializers.CharField()

class PasswordSerializer(serializers.Serializer):
    password = serializers.CharField()

class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField()