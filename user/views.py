from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from user.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
# Create your views here.
def user(request):
    return render(request, 'user.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            #LOG THE USER IN HERE
            return redirect('homepage')
        
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == ('POST'):
        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if form.is_valid:
                login(request, user)
                return redirect('homepage')
        else:
            messages.error(request,'username or password incorrect')
            return redirect('login')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


