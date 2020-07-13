from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def login_request(request):
    if request.method == "POST":
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

    form = AuthenticationForm
    return render(request=request,
                  template_name="main/login.html",
                  context={"form": form})

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("main:homepage")