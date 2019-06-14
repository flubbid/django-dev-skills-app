from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
# Create your views here.
def home(request):
    return render(request, 'home.html')

# todo add error message for the view function on login incorrectg
def signup(request):
    if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                #login the user
                #redirect
                login(request, user)
                redirect('home')
                return redirect('home')
    # Todo need to refactor to post form to database
    form = UserCreationForm
    return render(request, 'signup.html', {'form': form})
