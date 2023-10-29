from django.core.validators import MinValueValidator, MaxValueValidator
from rest_framework.fields import IntegerField
from rest_framework.serializers import ModelSerializer

from youtube_clone.models import Video


class VideoCreateModelSerializer(ModelSerializer):
    duration = IntegerField(validators=[
        MinValueValidator(1), MaxValueValidator(43200)
    ], read_only=True, help_text='Duration in seconds (e.g. 43200 for 12 hours)')  # video duration

    def validate(self, attrs):
        return super().validate(attrs)

    class Meta:
        model = Video
        exclude = ('views_count', 'channel')
