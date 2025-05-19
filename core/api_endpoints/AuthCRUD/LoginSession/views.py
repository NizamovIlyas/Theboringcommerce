# core/api_endpoints/AuthCRUD/Login/views.py

from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.middleware.csrf import get_token

class SessionLoginAPIView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []  # Disables default authentication

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(request, username=email, password=password)  # adjust if using custom user model
        if user is not None:
            login(request, user)
            csrf_token = get_token(request)
            return JsonResponse({
                'message': 'Login successful',
                'csrfToken': csrf_token
            })
        else:
            return JsonResponse({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
