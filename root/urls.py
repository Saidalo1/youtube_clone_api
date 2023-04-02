from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # admin
    path('admin/', admin.site.urls),

    # youtube_clone urls
    path('', include('youtube_clone.urls')),
]
