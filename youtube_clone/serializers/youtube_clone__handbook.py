from rest_framework.serializers import ModelSerializer

from youtube_clone.models import Category


class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        exclude = ()
