from django.contrib.auth.models import User
from django.db.models import Model, CharField, TextField, ForeignKey, OneToOneField, CASCADE, \
    FileField, DateTimeField


class Video(Model):
    title = CharField(max_length=255)
    description = TextField()
    category = ForeignKey('youtube_clone.Category', CASCADE)
    channel = ForeignKey('youtube_clone.Channel', CASCADE)


class Comment(Model):
    content = TextField()
    video = ForeignKey(Video, CASCADE)
    user = ForeignKey(User, CASCADE)


class VideoFile(Model):
    video = OneToOneField(Video, CASCADE)
    file = FileField(upload_to='videos/')
    created_at = DateTimeField(auto_now_add=True)
