from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return render(request,'home.html')

def add(request):
    val1 = int(request.GET['num1'])
    val2 = int(request.GET['num2'])
    val4 =(request.GET['val3'])
    if val4== "+" :
        res=val1+val2
    elif val4 == "-":
        res=val1-val2
    elif val4 == "*":
        res=val1*val2
    elif val4 == "/":
        res=val1//val2          

    return render(request,"operation.html",{"result":res})   
def fact(request):
    val5 = int(request.GET['num3'])
    fact=0
    while val5 > 1:
        fact= fact*val5
        val5-=1  
    res1=fact
    return render(request,"operation.html",{"result1":res1})    

# Create your views here.
