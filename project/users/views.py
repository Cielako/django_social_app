from pyexpat.errors import messages
from django.shortcuts import redirect, render

from users.forms import CustomUserCreationForm

# Create your views here.
def user(request):
    return render(request, "users/user.html")

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()


            return redirect('index')  # Przekierowanie na stronę główną po rejestracji
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})