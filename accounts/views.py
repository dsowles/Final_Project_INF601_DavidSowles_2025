from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm

def register_view(request):
    """
    Handles user registration. 
    Displays the form on GET request, processes the form on POST request.
    """
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto-login
            return redirect('home')  # Change to your homepage path
    else:
        form = RegisterForm()

    return render(request, "accounts/register.html", {"form": form})


def login_view(request):
    """
    Handles user login using Django's built-in AuthenticationForm.
    """
    if request.method == "POST":
        # Create an AuthenticationForm instance, bound to the request data
        # 'data=request.POST' is explicit and good practice for this form type
        form = AuthenticationForm(data=request.POST)
        # Check if the credentials provided are valid (this authenticates the user)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form = AuthenticationForm()

    return render(request, "accounts/login.html", {"form": form})


def logout_view(request):
    """
    Logs the user out and redirects them to the homepage.
    """
    logout(request)
    return redirect("home")