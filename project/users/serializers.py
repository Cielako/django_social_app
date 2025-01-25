from rest_framework import serializers
from .models import CustomUser

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, required=True)
    
class UserResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser  # lub Twój niestandardowy model użytkownika
        fields = ['id', 'username', 'email']  # Możesz dodać inne pola użytkownika, jeśli chcesz

class LoginResponseSerializer(serializers.Serializer):
    success = serializers.BooleanField()
    message = serializers.CharField()
    access_token = serializers.CharField()
    user = UserResponseSerializer()  # Możesz zwrócić dodatkowe informacje o użytkowniku
    
    def get_user(self, obj):
        return {
            'id': obj.id,
            'username': obj.username,
            'email': obj.email,
        }