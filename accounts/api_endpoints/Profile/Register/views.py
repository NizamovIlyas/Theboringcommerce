# Register/views.py
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import status, views
from rest_framework.response import Response
from .serializers import RegisterSerializer
from .tokens import verify_register_token
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny

User = get_user_model()

class RegisterAPIView(views.APIView):
    permission_classes = [AllowAny]
    @swagger_auto_schema(
        request_body=RegisterSerializer,
        responses={
            201: openapi.Response('Check your email to verify your account.'),
            400: 'Bad Request',
        }
    )
    def post(self, request):
        serializer = RegisterSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Check your email to verify your account."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# views.py
class VerifyEmailAPIView(views.APIView):
    permission_classes = [AllowAny]
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'token',
                openapi.IN_QUERY,
                description="Email verification token",
                type=openapi.TYPE_STRING,
                required=True
            )
        ],
        responses={
            200: openapi.Response("Email verified successfully"),
            400: "Invalid or expired token",
            404: "User not found"
        }
    )
    def get(self, request):
        token = request.query_params.get('token')
        if not token:
            return Response({"error": "Missing token"}, status=status.HTTP_400_BAD_REQUEST)

        user_id = verify_register_token(token)
        if user_id is None:
            return Response({"error": "Invalid or expired token"}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.filter(pk=user_id).first()
        if user:
            user.is_active = True
            user.is_email_verified = True
            user.save()
            return Response({"message": "Email verified successfully"})
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
