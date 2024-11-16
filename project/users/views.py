from pyexpat.errors import messages
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from users.forms import CustomUserCreationForm

@login_required  # Strona dla zalogowanych użytkowników
def user(request):
    user = request.user  # pobranie zalogowanego użytkownika
    return render(request, 'users/user.html', {'user': user})

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