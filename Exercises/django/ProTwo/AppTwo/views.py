from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    my_dict1 = {'insert_here':"Index page"}
    return render(request,'appTwo/help.html',context=my_dict1)

def help(request):
    my_dict = {'insert_here':"Help Page"}
    return render(request,'appTwo/help.html',context=my_dict)
