from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

posts=[
    {
        'model':'inspiron',
        'device':'laptop',
        'type':'college',
    },
    {
        'model':'legion',
        'device':'laptop',
        'type':'gaming',
    },
    {
        'model':'alienware',
        'device':'laptop',
        'type':'gaming',
    }

]
def home(request):
    context ={
        'posts':posts,
        'title':"home"
    }
    return render(request,'products/home.html',context)
def about(request):
    context ={
        'title':"about"
    }
    return render(request,'products/about.html',context)
