from django.shortcuts import render, redirect
from user.forms import UserCreationForm
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