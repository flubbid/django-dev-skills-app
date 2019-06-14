from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from .forms import LoginForm
# Create your views here.
def home(request):
    return render(request, 'home.html')

# todo add error message for the view function on login incorrect
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

def login_view(request):
    if request.method == 'POST':
        form= LoginForm(request.POST),
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                error_message = "Sorry, Your Username of Pssword was invalid!"
    
    form = LoginForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'login.html', context)

def logout_view(request):
    logout(request)
    return redirect('home')