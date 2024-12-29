from django.urls import path
from . import views

from django.contrib.auth import views as auth_views
from users.backends import UsernameOrEmailBackend
urlpatterns = [
    path('login/', views.login, name='login'),  # Widok logowania
    path('register/', views.register, name='register'), # Widok rejestracji 
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),  # Widok wylogowania
    path('user/', views.user, name='user'),
]
