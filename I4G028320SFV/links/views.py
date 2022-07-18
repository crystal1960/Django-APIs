from .serializers import LinkSerializer
from .models import Links

from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DetailAPIView
from rest_framework.generics import UpdateAPIView
from rest_framework.generics import DeleteAPIView

class PostListApi (ListAPIView):

    queryset = Links.objects.filter(active=True)
    serializer_class = LinkSerializer

class PostCreateApi (CreateAPIView):

    queryset = Links.objects.filter(active=True)
    serializer_class = LinkSerializer

class PostDetailApi (DetailAPIView):

    queryset = Links.objects.filter(active=True)
    serializer_class = LinkSerializer

class PostUpdateApi (UpdateAPIView):

    queryset = Links.objects.filter(active=True)
    serializer_class = LinkSerializer

class PostDeleteApi (DeleteAPIView):

    queryset = Links.objects.filter(active=True)
    serializer_class = LinkSerializer

