from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,get_user_model
from django.contrib.auth.decorators import login_required
import datetime
from django.core.urlresolvers import reverse

User = get_user_model()

@login_required
def index(request):
    users = User.objects.select_related('logged_in_user')
    for user in users:
        user.status = 'Online' if hasattr(user, 'logged_in_user') else 'Offline'
    return render(request, 'accounts/index.html', {'users': users})

def login_views(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect(reverse('home'))
        else:
            print(form.errors)
    else:
        form = AuthenticationForm()
    return render(request,'registration/login.html',{'form':form})

def logout_views(request):
    logout(request)
    return redirect('accounts:login')
