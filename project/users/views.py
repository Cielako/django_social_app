from pyexpat.errors import messages
from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.contrib.auth import login as auth_login
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
# Custom user authentication 
from users.backends import UsernameOrEmailBackend

from users.forms import CustomUserCreationForm


@login_required  # Strona dla zalogowanych użytkowników
def user(request):
    user = request.user  # pobranie zalogowanego użytkownika
    return render(request, 'users/user.html', {'user': user})


def login(request):
    '''
    Simple ajax_login function - we refreshing only part of page instead of all 
    '''
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