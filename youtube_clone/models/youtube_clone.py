from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Model, CharField, TextField, ForeignKey, CASCADE, \
    FileField, ManyToManyField, ImageField, DateTimeField, URLField, PositiveIntegerField

from shared.django import TimeBaseModel, VideoBaseModel


class Video(VideoBaseModel):
    tags = ManyToManyField('youtube_clone.Tag', 'videos', blank=True)
    video_file = FileField(upload_to='videos/')
    duration = PositiveIntegerField(validators=[
        MinValueValidator(1), MaxValueValidator(43200)
    ], help_text='Duration in seconds (e.g. 43200 for 12 hours)')  # video duration

    def __str__(self):
        return self.title


class Channel(TimeBaseModel):
    name = CharField(max_length=255)
    description = TextField()
    owner = ForeignKey(User, CASCADE, 'owned_channels', db_index=True)
    image = ImageField(upload_to='channel_images', null=True, blank=True)
    banner = ImageField(upload_to='channel_banners', null=True, blank=True)

    def __str__(self):
        return self.name


class LiveStream(Model):
    title = CharField(max_length=255)
    description = TextField()
    start_time = DateTimeField()
    end_time = DateTimeField()
    url = URLField()

    def __str__(self):
        return self.title


class ShortVideo(VideoBaseModel):
    tags = ManyToManyField('youtube_clone.Tag', 'short_videos', blank=True)
    video_file = FileField(upload_to='short_videos/')
    duration = PositiveIntegerField(validators=[
        MinValueValidator(1), MaxValueValidator(60)
    ], help_text='Duration in seconds (e.g. 60 for 1 minute)')  # video duration

    def __str__(self):
        return self.title
