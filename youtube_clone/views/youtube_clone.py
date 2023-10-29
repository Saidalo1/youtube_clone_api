from rest_framework.generics import CreateAPIView
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated

from youtube_clone.models import Video
from youtube_clone.serializers import VideoCreateModelSerializer


class VideoCreateAPIView(CreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoCreateModelSerializer
    permission_classes = (IsAuthenticated,)
    parser_classes = (MultiPartParser,)
