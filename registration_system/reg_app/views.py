from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login')
def HomePageView(request):
    return render(request, 'home.html')

def SignInView(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        pass1 = request.POST.get('pass')
        print(uname, pass1)
        user = authenticate(request, username=uname, password=pass1)
        print(user, "==user")
        if user is not None:
            login(request, user)
            return redirect('home')
        else:   
            return HttpResponse("Username or Password is incorrect!")
    return render(request, 'login.html')

def SignUpView(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        print(uname, email, pass1, pass2)
        if pass1 == pass2:
            my_user = User.objects.create_user(uname, email, pass1)
            my_user.first_name = first_name
            my_user.last_name = last_name
            my_user.save()
            return redirect('login')
        else:
            return HttpResponse("Passwords do not match!")
    return render(request, 'signup.html') 

def LogoutView(request):
    logout(request)
    return redirect('login')