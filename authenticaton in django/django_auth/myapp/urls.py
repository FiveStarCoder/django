from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
    path('',views.home_page, name='home'),
    path('login',views.login_page, name='login'),
    path('logout',views.logout_page, name='logout'),
    
]
