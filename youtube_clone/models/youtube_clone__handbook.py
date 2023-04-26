from django.contrib.auth.models import User
from django.db.models import Model, CharField, TextField, ForeignKey, CASCADE, TextChoices, DateTimeField, \
    ManyToManyField, DecimalField, PositiveIntegerField
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Category(Model):
    name = CharField(max_length=255)
    description = TextField()


class VideoLikeDislikeUser(Model):
    class LikeDislikeChoices(TextChoices):
        LIKE = 'like', 'like'
        DISLIKE = 'dislike', 'dislike'

    user = ForeignKey(User, CASCADE, db_index=True)
    video = ForeignKey('youtube_clone.Video', CASCADE, db_index=True)
    choice = CharField(max_length=7, choices=LikeDislikeChoices.choices)

    class Meta:
        unique_together = ('user', 'video')


class ShortVideoLikeDislikeUser(Model):
    class LikeDislikeChoices(TextChoices):
        LIKE = 'like', 'like'
        DISLIKE = 'dislike', 'dislike'

    user = ForeignKey(User, CASCADE, db_index=True)
    short_video = ForeignKey('youtube_clone.ShortVideo', CASCADE, db_index=True)
    choice = CharField(max_length=7, choices=LikeDislikeChoices.choices)

    class Meta:
        unique_together = ('user', 'short_video')


class Tag(Model):
    name = CharField(max_length=255)


class VideoComment(MPTTModel):
    content = TextField()
    video = ForeignKey('youtube_clone.Video', CASCADE, db_index=True)
    user = ForeignKey(User, CASCADE, db_index=True)
    parent = TreeForeignKey('self', CASCADE, 'children', null=True, blank=True)

    class MPTTMeta:
        order_insertion_by = ['id']


class ShortVideoComment(MPTTModel):
    content = TextField()
    short_video = ForeignKey('youtube_clone.ShortVideo', CASCADE, db_index=True)
    user = ForeignKey(User, CASCADE, db_index=True)
    parent = TreeForeignKey('self', CASCADE, 'children', null=True, blank=True)

    class MPTTMeta:
        order_insertion_by = ['id']


class VideoCommentLikeDislikeUser(Model):
    class LikeDislikeChoices(TextChoices):
        LIKE = 'like', 'like'
        DISLIKE = 'dislike', 'dislike'

    user = ForeignKey(User, CASCADE, db_index=True)
    video_comment = ForeignKey('youtube_clone.VideoComment', CASCADE, 'likes_dislikes', db_index=True)
    choice = CharField(max_length=7, choices=LikeDislikeChoices.choices)

    class Meta:
        unique_together = ('user', 'video_comment')


class ShortVideoCommentLikeDislikeUser(Model):
    class LikeDislikeChoices(TextChoices):
        LIKE = 'like', 'like'
        DISLIKE = 'dislike', 'dislike'

    user = ForeignKey(User, CASCADE, db_index=True)
    short_video_comment = ForeignKey('youtube_clone.ShortVideoComment', CASCADE, 'likes_dislikes', db_index=True)
    choice = CharField(max_length=7, choices=LikeDislikeChoices.choices)

    class Meta:
        unique_together = ('user', 'short_video_comment')


class Playlist(Model):
    title = CharField(max_length=255)
    description = TextField()
    videos = ManyToManyField('youtube_clone.Video')


class Subscription(Model):
    user = ForeignKey(User, CASCADE, related_name='subscriptions')
    channel = ForeignKey('youtube_clone.Channel', CASCADE, related_name='subscribers')
    created_at = DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'channel']


class Map(Model):
    title = CharField(max_length=255)
    description = TextField()
    latitude = DecimalField(max_digits=9, decimal_places=6)
    longitude = DecimalField(max_digits=9, decimal_places=6)
    zoom_level = PositiveIntegerField()
