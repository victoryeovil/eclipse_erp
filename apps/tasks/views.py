from rest_framework import generics
from .models import Task, Media
from .serializers import TaskSerializer, MediaSerializer

class TaskListCreateAPIView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class MediaListCreateAPIView(generics.ListCreateAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer

class MediaRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer
