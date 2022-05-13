from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('regiter/', views.registerUser, name="register"),
    path('profile/<str:pk>', views.profile, name="profile"),
    path('account/', views.userAccount, name='account'),
    path('edit-account/', views.editAccount, name="edit-account")
]