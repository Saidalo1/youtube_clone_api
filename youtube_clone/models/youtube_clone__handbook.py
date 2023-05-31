from django.contrib.auth.models import User
from django.db.models import CharField, TextField, ForeignKey, CASCADE, TextChoices, ManyToManyField, DecimalField, \
    PositiveIntegerField
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from shared.django import TimeBaseModel


class Category(TimeBaseModel):
    name = CharField(max_length=255)
    description = TextField()


class VideoLikeDislikeUser(TimeBaseModel):
    class LikeDislikeChoices(TextChoices):
        LIKE = 'like', 'like'
        DISLIKE = 'dislike', 'dislike'

    user = ForeignKey(User, CASCADE, db_index=True)
    video = ForeignKey('youtube_clone.Video', CASCADE, db_index=True)
    choice = CharField(max_length=7, choices=LikeDislikeChoices.choices)

    class Meta:
        unique_together = ('user', 'video')


class ShortVideoLikeDislikeUser(TimeBaseModel):
    class LikeDislikeChoices(TextChoices):
        LIKE = 'like', 'like'
        DISLIKE = 'dislike', 'dislike'

    user = ForeignKey(User, CASCADE, db_index=True)
    short_video = ForeignKey('youtube_clone.ShortVideo', CASCADE, db_index=True)
    choice = CharField(max_length=7, choices=LikeDislikeChoices.choices)

    class Meta:
        unique_together = ('user', 'short_video')


class Tag(TimeBaseModel):
    name = CharField(max_length=255)


class VideoComment(TimeBaseModel, MPTTModel):
    content = TextField()
    video = ForeignKey('youtube_clone.Video', CASCADE, db_index=True)
    user = ForeignKey(User, CASCADE, db_index=True)
    parent = TreeForeignKey('self', CASCADE, 'children', null=True, blank=True)

    class MPTTMeta:
        order_insertion_by = ['id']


class ShortVideoComment(TimeBaseModel, MPTTModel):
    content = TextField()
    short_video = ForeignKey('youtube_clone.ShortVideo', CASCADE, db_index=True)
    user = ForeignKey(User, CASCADE, db_index=True)
    parent = TreeForeignKey('self', CASCADE, 'children', null=True, blank=True)

    class MPTTMeta:
        order_insertion_by = ['id']


class VideoCommentLikeDislikeUser(TimeBaseModel):
    class LikeDislikeChoices(TextChoices):
        LIKE = 'like', 'like'
        DISLIKE = 'dislike', 'dislike'

    user = ForeignKey(User, CASCADE, db_index=True)
    video_comment = ForeignKey('youtube_clone.VideoComment', CASCADE, 'likes_dislikes', db_index=True)
    choice = CharField(max_length=7, choices=LikeDislikeChoices.choices)

    class Meta:
        unique_together = ('user', 'video_comment')


class ShortVideoCommentLikeDislikeUser(TimeBaseModel):
    class LikeDislikeChoices(TextChoices):
        LIKE = 'like', 'like'
        DISLIKE = 'dislike', 'dislike'

    user = ForeignKey(User, CASCADE, db_index=True)
    short_video_comment = ForeignKey('youtube_clone.ShortVideoComment', CASCADE, 'likes_dislikes', db_index=True)
    choice = CharField(max_length=7, choices=LikeDislikeChoices.choices)

    class Meta:
        unique_together = ('user', 'short_video_comment')


class Playlist(TimeBaseModel):
    title = CharField(max_length=255)
    description = TextField()
    videos = ManyToManyField('youtube_clone.Video')


class Subscription(TimeBaseModel):
    user = ForeignKey(User, CASCADE, related_name='subscriptions')
    channel = ForeignKey('youtube_clone.Channel', CASCADE, related_name='subscribers')

    class Meta:
        unique_together = ['user', 'channel']


class Map(TimeBaseModel):
    title = CharField(max_length=255)
    description = TextField()
    latitude = DecimalField(max_digits=9, decimal_places=6)
    longitude = DecimalField(max_digits=9, decimal_places=6)
    zoom_level = PositiveIntegerField()
