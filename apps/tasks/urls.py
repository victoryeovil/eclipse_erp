from django.urls import path
from .views import TaskListCreateAPIView, TaskRetrieveUpdateDestroyAPIView, MediaListCreateAPIView, MediaRetrieveUpdateDestroyAPIView


urlpatterns = [
    path('tasks/', TaskListCreateAPIView.as_view(), name='task_list'),
    path('tasks/<int:pk>/', TaskRetrieveUpdateDestroyAPIView.as_view(), name='task_detail'),
    path('media/', MediaListCreateAPIView.as_view(), name='media_list'),
    path('media/<int:pk>/', MediaRetrieveUpdateDestroyAPIView.as_view(), name='media_detail'),
]
