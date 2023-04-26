from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db.models import Model, CharField, TextField, ForeignKey, CASCADE, \
    FileField, ManyToManyField, ImageField, IntegerField, PositiveIntegerField, DateTimeField, URLField


class Video(Model):
    title = CharField(max_length=255)
    description = TextField()
    category = ForeignKey('youtube_clone.Category', CASCADE, db_index=True)
    channel = ForeignKey('youtube_clone.Channel', CASCADE, db_index=True)
    tags = ManyToManyField('youtube_clone.Tag', 'videos', blank=True)
    video_file = FileField(upload_to='videos/')
    views_count = IntegerField(default=0, validators=[MinValueValidator(0)])
    duration = PositiveIntegerField()  # video duration


class Channel(Model):
    name = CharField(max_length=255)
    description = TextField()
    owner = ForeignKey(User, CASCADE, 'owned_channels', db_index=True)
    image = ImageField(upload_to='channel_images', null=True, blank=True)
    banner = ImageField(upload_to='channel_banners', null=True, blank=True)


class LiveStream(Model):
    title = CharField(max_length=255)
    description = TextField()
    start_time = DateTimeField()
    end_time = DateTimeField()
    url = URLField()


class ShortVideo(Model):
    title = CharField(max_length=255)
    description = TextField()
    category = ForeignKey('youtube_clone.Category', CASCADE)
    channel = ForeignKey('youtube_clone.Channel', CASCADE)
    tags = ManyToManyField('youtube_clone.Tag', 'short_videos')
    video_file = FileField(upload_to='short_videos/')
    views_count = IntegerField(default=0, validators=[MinValueValidator(0)])
    duration = PositiveIntegerField()  # short video duration
