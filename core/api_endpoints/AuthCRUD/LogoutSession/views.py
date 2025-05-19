# core/api_endpoints/AuthCRUD/Logout/views.py
from django.contrib.auth import logout
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.http import JsonResponse

class SessionLogoutAPIView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []  # Optional: remove if you want to restrict logout to authenticated users

    def post(self, request):
        logout(request)
        return JsonResponse({'message': 'Logout successful'})
