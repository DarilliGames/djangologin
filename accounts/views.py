from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages, auth

from .forms import UserLoginForm, UserRegistrationForm

# Create your views here.
def get_index(request):
    return render(request, "accounts/index.html")
    
def create_account(request):
    return "Hello Human"

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            user = auth.authenticate(username=request.POST.get('username'),
                                     password=request.POST.get('password1'))

            if user:
                auth.login(request, user)
                messages.success(request, "You have successfully registered")
                return redirect('profile')

            else:
                messages.error(request, "unable to log you in at this time!")

    else:
        form = UserRegistrationForm()

    return render(request, 'accounts/register.html', {'form': form})  




def login_accounts(request):
    if request.method == "POST":
        print("You are posting")
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user= auth.authenticate(username=request.POST.get("username"),
                                    password=request.POST.get("password"))
            
            if user is not None:
                auth.login(request, user)
                print("Logged in- - " + user.username)
                return redirect("/")
            else:
                print("Null Found")
                form.add_error(None, "Either your Username of Password was not recognised or typed incorrectly")
    else:
        form = UserLoginForm()
        print("this is a get")
    return render(request, "accounts/loggin.html", {"form":form})
    
def logout(request):
    auth.logout(request)
    return render(request, "accounts/logout.html")

def get_profile(request):
    return render(request, "accounts/profile.html")