from pyexpat.errors import messages
from django.contrib import messages

from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required


# Custom user authentication 
from users.backends import UsernameOrEmailBackend
from users.forms import CustomUserCreationForm

from django.utils.translation import gettext_lazy as _

#API 
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from users.serializers import LoginResponseSerializer, LoginSerializer, UserResponseSerializer


@login_required  # Strona dla zalogowanych użytkowników
def user(request):
    user = request.user  # pobranie zalogowanego użytkownika
    return render(request, 'users/user.html', {'user': user})

class LoginAPIView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        # Autentykacja użytkownika
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Generowanie tokenu JWT
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)

            # Zwrócenie odpowiedzi z tokenem oraz informacją o sukcesie
            data = {
                'success': True,
                'access_token': access_token,
                'redirect_url': '/dashboard',  # Przekierowanie na stronę
                'message': 'Zalogowano pomyślnie'
            }

            return Response(data, status=status.HTTP_200_OK)
        
        return Response({
            'success': False,
            'error': 'Nieprawidłowe dane logowania',
            'message': 'Spróbuj ponownie z poprawnymi danymi.'
        }, status=status.HTTP_401_UNAUTHORIZED)


def login(request):
    '''
    Simple ajax_login function - we refreshing only part of page instead of all 
    '''
    
    if(request.user.is_authenticated):
        messages.error(request, 'Użytkownik jest już zalogowany')
        return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            # Utwórz instancję backendu
            backend = UsernameOrEmailBackend()
            
            # Wywołaj metodę authenticate z instancji backendu
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                auth_login(request, user)  # Użyj funkcji `auth_login`, aby nie było konfliktu z nazwą widoku
                return redirect('user_dashboard')  # Przekierowanie po poprawnym zalogowaniu
                #return JsonResponse({'success': True})
            else:
                return JsonResponse({'success': False, 'error': 'Podane dane logowania są nieprawidłowe'})
        
        return JsonResponse({'success': False, 'error': 'Metoda nieobsługiwana'})



def register(request):
    if request.user.is_authenticated:
        # Jesli zalogowany, to nie może tworzyć konta i zostaje przekierowany na panel
        return redirect('user')
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Przekierowanie na stronę główną po rejestracji
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})