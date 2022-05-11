from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.discussion, name="discussion"),
    # path('topic/', views.topic, name="topic"),
    path('rooms/', views.rooms, name="rooms"),
    path('room/<str:pk>', views.room, name="room"),
    path('create-room', views.createRoom, name="create-room"),
    path('update-room/<str:pk>', views.updateRoom, name="update-room"),
    path('delete-room/<str:pk>', views.deleteRoom, name="delete-room"),
    path('create-question', views.createQuestion, name="create-question"),
    path('update-question/<str:pk>', views.updateQuestion, name="update-question"),
    path('delete-question/<str:pk>', views.deleteQuestion, name="delete-question"),
    path('create-answer', views.createAnswer, name="create-answer"),
    path('update-answer/<str:pk>', views.updateAnswer, name="update-answer"),
    path('delete-answer/<str:pk>', views.deleteAnswer, name="delete-answer")
]