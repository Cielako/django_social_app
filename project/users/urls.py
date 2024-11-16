from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),  # Widok logowania
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),  # Widok wylogowania
    path('register/', views.register, name='register'),
    path('user/', views.user, name='user'),
]
