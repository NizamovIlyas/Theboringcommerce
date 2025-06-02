# Register/serializers.py
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .tokens import generate_register_token
from .email_send import send_register_confirm_email

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["email", "password"]

    def create(self, validated_data):
        user = User.objects._create_user(**validated_data)
        user.is_active = False  # user must verify email
        user.save()

        token = generate_register_token(user)
        send_register_confirm_email(user.email, token)

        return user
