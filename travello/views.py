from itertools import count
from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .models import destination, location

# Create your views here.
def index(request):
    dests=destination.objects.all() 
    return render(request,'index.html',{'dests':dests})

def destinations(request):
        loc=location.objects.all()
        if  request.user.is_authenticated:
            return render(request,'destinations.html',{'loc':loc})
        else:
            return redirect('login')     
        


