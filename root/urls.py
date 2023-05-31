from django.contrib import admin
from django.urls import path, include
from drf_yasg.openapi import License, Info, Contact
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny

# Configure the Swagger/OpenAPI documentation
schema_view = get_schema_view(
    Info(
        title="VidTube API Documentation",
        default_version='v1',
        description="VidTube is an innovative video platform that offers seamless streaming and engaging content "
                    "discovery for users.",
        terms_of_service="https://www.example.com/policies/terms/",
        contact=Contact(email="vidtubecontactinfo@gmail.com"),
        license=License(name="MIT License"),
    ),
    public=True,
    permission_classes=[AllowAny]
)

urlpatterns = [
    # admin
    path('admin/', admin.site.urls),

    # youtube_clone urls
    path('', include('youtube_clone.urls')),

    # auth
    path('accounts/', include('users.urls')),

    # swagger
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
