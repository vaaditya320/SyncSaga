from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url="login/")
def dashboard_view(request):
    first_name = request.user.first_name
    return render(request, 'dashboard.html', {'first_name': first_name})
