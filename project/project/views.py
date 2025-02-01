from django.shortcuts import render
from django.shortcuts import redirect

def index(request):
    return render(request, 'index.html')

def change_language(request):
    lang_code = request.GET.get('lang', 'en')  # Domyślnie 'en'
    response = redirect(request.META.get('HTTP_REFERER', '/'))  # Wróć na poprzednią stronę
    response.set_cookie('django_language', lang_code)  # Zapisz język w cookies
    return response