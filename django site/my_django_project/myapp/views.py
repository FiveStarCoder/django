from django.shortcuts import render, HttpResponse
from myapp.models import Contact
from datetime import datetime
from django.contrib import messages

# Create your views here.


def home(request):
    # return HttpResponse("This is home page")
    context = {
        'username': "Muhammad Asif Ali"
    }

    
    return render(request,"index.html",context)

def about(request):
    # return HttpResponse("This is about page")
    return render(request,'about.html')

def contact(request):
    # return HttpResponse("This is contact page")

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        contact = Contact(name=name, email=email, phone=phone,message=message, date = datetime.now())
        contact.save() # saves the information

        messages.success(request,"Your messages has been sent! Thank you for your message")
        



    return render(request,'contact.html')

def services(request):
    # return HttpResponse("This is Services Page")
    return render(request,'services.html')