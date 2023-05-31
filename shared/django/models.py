from django.core.validators import MinValueValidator
from django.db.models import Model, DateTimeField, CharField, TextField, ForeignKey, ManyToManyField, FileField, \
    IntegerField, PositiveIntegerField, CASCADE


class TimeBaseModel(Model):
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class VideoBaseModel(TimeBaseModel):
    title = CharField(max_length=255)
    description = TextField()
    category = ForeignKey('youtube_clone.Category', CASCADE, db_index=True)
    channel = ForeignKey('youtube_clone.Channel', CASCADE, db_index=True)
    tags = ManyToManyField('youtube_clone.Tag', '', blank=True)
    video_file = FileField(upload_to='')
    views_count = IntegerField(default=0, validators=[MinValueValidator(0)])
    duration = PositiveIntegerField(default=0)  # video duration

    class Meta:
        abstract = True
