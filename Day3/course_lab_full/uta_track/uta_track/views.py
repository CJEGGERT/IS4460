from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from uta_user.models import UtaUser

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            uta_user = UtaUser.objects.create(auth_user=user) # create out custom user info
            auth_login(request, user)
            return redirect('home')  # Redirect to a home or other page
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
