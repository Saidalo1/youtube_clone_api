from rest_framework.viewsets import ReadOnlyModelViewSet

from youtube_clone.models import Category
from youtube_clone.serializers import CategoryModelSerializer


class CategoryReadOnlyModelViewSet(ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
