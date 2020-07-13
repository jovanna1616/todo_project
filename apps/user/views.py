from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from .forms import NewUserForm

# Create your views here.
@require_http_methods(["GET"])
def login_form(request):
    form = AuthenticationForm
    return render(request=request,
                  template_name="main/login.html",
                  context={"form": form})

@require_http_methods(["POST"])
def login_request(request):
    form = AuthenticationForm(request, data=request.POST)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.info(request, f"You logged in with username {username}")
            return redirect("main:homepage")
        else:
            messages.error(request, f"Login attempt for username {username} failed.")
    else:
        messages.error(request, "Invalid username or password")

@require_http_methods(["GET"])
def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("main:homepage")

@require_http_methods(["GET"])
def register_form(request):
    form = NewUserForm
    return render(request=request,
                  template_name="main/register.html",
                  context={"form": form})

@require_http_methods(["POST"])
def register_request(request):
    form = NewUserForm(request.POST)
    if form.is_valid():
        user = form.save()
        login(request, user)
        username = form.cleaned_data.get("username")
        messages.info(request, f"You registered and logged in with username {username}")
        return redirect("main:homepage")
    else:
        for message in form.error_messages:
            message.error(request, f"{message}: {form.error_messages[message]}")
    