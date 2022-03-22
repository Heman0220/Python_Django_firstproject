from imaplib import _Authenticator
from operator import is_not
from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages



def login(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password = password)
        
        if user is not None:
            if user.is_active:
                auth.login(request,user)
                return redirect('/')
        else:
            messages.info(request,"id not exist")
            return redirect('login')    
    else:    
        return render(request,'login.html')

def register(request):

    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['second_name']
        username=request.POST['user_name']
        email=request.POST['mail']
        password=request.POST['password1']
        password2=request.POST['password2']
        print("user name",username,"password",password)
        if password==password2:     
            if User.objects.filter(username=username).exists():
                messages.info(request,"user name already exist")
                return redirect('register')   
            elif User.objects.filter(email=email).exists():
                messages.info(request,"mail already taken") 
                return redirect('register')      
            else:    
                user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
                user.save();
                return redirect('login')
        else:
            messages.info(request,"password not vaild") 
            return redirect('register')       
    else:
      return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')  

def about(request):
    user=User.objects
    if  request.user.is_authenticated:
        return render(request,'about.html',{'user':user})
    else:
        return redirect('login')    


 




