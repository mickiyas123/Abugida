from django.urls import path
from . import views

urlpatterns = [
    path('', views.discussions, name="discussions"),
    path('create-room/', views.createRoom, name="create-room"),

    
    
]
