from django.contrib.auth.models import User
from django.db.models import Model, CharField, TextField, ForeignKey, CASCADE, ManyToManyField


class Category(Model):
    name = CharField(max_length=255)
    description = TextField()


class Channel(Model):
    name = CharField(max_length=255)
    description = TextField()
    owner = ForeignKey(User, CASCADE, 'owned_channels')
    subscribers = ManyToManyField(User, 'subscribed_to')


class VideoLikeDislikeUser(Model):
    LIKE = 'like'
    DISLIKE = 'dislike'
    CHOICES = (
        (LIKE, 'Like'),
        (DISLIKE, 'Dislike')
    )

    user = ForeignKey(User, CASCADE)
    video = ForeignKey('youtube_clone.Video', CASCADE)
    choice = CharField(choices=CHOICES, max_length=7)
