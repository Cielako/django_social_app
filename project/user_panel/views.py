from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def user_dashboard(request):
    return render(request, 'user_panel/dashboard.html')
