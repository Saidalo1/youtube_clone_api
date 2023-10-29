from django.contrib.auth.models import User
from django.db.models import CharField, TextField, ForeignKey, CASCADE, TextChoices, ManyToManyField, DecimalField, \
    PositiveIntegerField
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from shared.django import TimeBaseModel


class Category(TimeBaseModel):
    name = CharField(max_length=255)

    def __str__(self):
        return self.name


class VideoLikeDislikeUser(TimeBaseModel):
    class LikeDislikeChoices(TextChoices):
        LIKE = 'like', 'like'
        DISLIKE = 'dislike', 'dislike'

    user = ForeignKey(User, CASCADE, db_index=True)
    video = ForeignKey('youtube_clone.Video', CASCADE, db_index=True)
    choice = CharField(max_length=7, choices=LikeDislikeChoices.choices)

    def __str__(self):
        return f'{self.user} - {self.video} - {self.choice}'

    @property
    def is_like(self):
        return self.choice == self.LikeDislikeChoices.LIKE

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

    def __str__(self):
        return f'{self.user} - {self.short_video} - {self.choice}'


class Tag(TimeBaseModel):
    name = CharField(max_length=255)

    def __str__(self):
        return self.name


class VideoComment(TimeBaseModel, MPTTModel):
    content = TextField()
    video = ForeignKey('youtube_clone.Video', CASCADE, db_index=True)
    user = ForeignKey(User, CASCADE, db_index=True)
    parent = TreeForeignKey('self', CASCADE, 'children', null=True, blank=True)

    class MPTTMeta:
        order_insertion_by = ['id']

    def __str__(self):
        return self.content


class ShortVideoComment(TimeBaseModel, MPTTModel):
    content = TextField()
    short_video = ForeignKey('youtube_clone.ShortVideo', CASCADE, db_index=True)
    user = ForeignKey(User, CASCADE, db_index=True)
    parent = TreeForeignKey('self', CASCADE, 'children', null=True, blank=True)

    class MPTTMeta:
        order_insertion_by = ['id']

    def __str__(self):
        return self.content


class VideoCommentLikeDislikeUser(TimeBaseModel):
    class LikeDislikeChoices(TextChoices):
        LIKE = 'like', 'like'
        DISLIKE = 'dislike', 'dislike'

    user = ForeignKey(User, CASCADE, db_index=True)
    video_comment = ForeignKey('youtube_clone.VideoComment', CASCADE, 'likes_dislikes', db_index=True)
    choice = CharField(max_length=7, choices=LikeDislikeChoices.choices)

    class Meta:
        unique_together = ('user', 'video_comment')

    def __str__(self):
        return f'{self.user} - {self.video_comment} - {self.choice}'


class ShortVideoCommentLikeDislikeUser(TimeBaseModel):
    class LikeDislikeChoices(TextChoices):
        LIKE = 'like', 'like'
        DISLIKE = 'dislike', 'dislike'

    user = ForeignKey(User, CASCADE, db_index=True)
    short_video_comment = ForeignKey('youtube_clone.ShortVideoComment', CASCADE, 'likes_dislikes', db_index=True)
    choice = CharField(max_length=7, choices=LikeDislikeChoices.choices)

    class Meta:
        unique_together = ('user', 'short_video_comment')

    def __str__(self):
        return f'{self.user} - {self.short_video_comment} - {self.choice}'


class Playlist(TimeBaseModel):
    title = CharField(max_length=255)
    description = TextField()
    videos = ManyToManyField('youtube_clone.Video')
    channel = ForeignKey('youtube_clone.Channel', CASCADE, db_index=True)

    def __str__(self):
        return self.title


class Subscription(TimeBaseModel):
    user = ForeignKey(User, CASCADE, related_name='subscriptions')
    channel = ForeignKey('youtube_clone.Channel', CASCADE, related_name='subscribers')

    class Meta:
        unique_together = ['user', 'channel']

    def __str__(self):
        return f'{self.user} - {self.channel}'


class Map(TimeBaseModel):
    title = CharField(max_length=255)
    description = TextField()
    latitude = DecimalField(max_digits=9, decimal_places=6)
    longitude = DecimalField(max_digits=9, decimal_places=6)
    zoom_level = PositiveIntegerField()

    def __str__(self):
        return self.title
