from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def home(request): 
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login Successful!")
            return redirect('home')
        else:
            messages.success(request, "Error logging in, please try again.")
            return redirect('home')
        
    else:
        return render(request, 'home.html', {})


def logout_user(request):
    pass