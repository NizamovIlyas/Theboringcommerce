from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions


from django.conf.urls import handler400, handler403, handler404, handler500
from django.shortcuts import render

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

schema_view = get_schema_view(
   openapi.Info(
      title="BoringCommerce API",
      default_version='v1',
      description="BoringCommerce platform API documentation",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="admin@@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
   authentication_classes=[],
)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('products/', include('products.urls')),
    path('admin/', admin.site.urls),
    # Swagger and Redoc URLs
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

def custom_bad_request(request, exception):
    return render(request, "400.html", status=400)

def custom_permission_denied(request, exception):
    return render(request, "403.html", status=403)

def custom_page_not_found(request, exception):
    return render(request, "404.html", status=404)

def custom_server_error(request):
    return render(request, "500.html", status=500)

handler400 = custom_bad_request
handler403 = custom_permission_denied
handler404 = custom_page_not_found
handler500 = custom_server_error
