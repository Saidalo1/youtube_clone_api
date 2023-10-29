from django.urls import path
from rest_framework.routers import DefaultRouter

from youtube_clone.views import CategoryReadOnlyModelViewSet, VideoCreateAPIView

router = DefaultRouter()
router.register(r'categories', CategoryReadOnlyModelViewSet, 'category')

urlpatterns = [
    path('create-video/', VideoCreateAPIView.as_view(), name='category')
              ] + router.urls
