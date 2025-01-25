from django.urls import path
from . import views

from django.contrib.auth import views as auth_views
from users.backends import UsernameOrEmailBackend
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
urlpatterns = [
        # Widoki JWT (dla tokenu dostępu i odświeżania)
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Uzyskanie tokenu dostępu
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Odświeżenie tokenu
    # Twój własny widok logowania
    path('login/', views.LoginAPIView.as_view(), name='login'),
    #path('login/', views.login, name='login'),  # Widok logowania
    path('register/', views.register, name='register'), # Widok rejestracji 
    #path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),  # Widok wylogowania
    #path('user/', views.user, name='user'),
]
