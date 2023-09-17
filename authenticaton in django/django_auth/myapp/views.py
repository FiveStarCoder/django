from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout, login

# Create your views here.
def home_page(request):
    if request.user.is_anonymous:
        print(request.user.is_anonymous)
     # Do something for authenticated users.
        return redirect('/login')
  
    return render(request,'index.html')

def login_page(request):

    if request.method =='POST':
        # check if the user entered the correct information
        username = request.POST.get('uname')
        psw = request.POST.get('psw')
        print(f"Name  is = {1}\nPassword is:{2}".format(username,psw))

        user = authenticate(username=username, password = psw)
        if user is not None:
        # A backend authenticated the credentials
            login(request, user)            
            return redirect('/')
    
        else:
        # No backend authenticated the credentials
            return render(request,'login.html')

       

    return render(request,'login.html')

def logout_page(request):
    logout(request)
    return redirect('/login')