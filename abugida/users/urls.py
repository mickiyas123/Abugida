from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('signup/', views.signupPage, name="signup"),
    path('about/', views.aboutPage, name="about"),
    path('courses/', views.coursesPage, name="courses"),

    ]