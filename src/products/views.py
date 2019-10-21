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

def xps(request):
    # This handles the AJAX POST from xps-webpage.html

    data = dict(request.POST)

    try:
        """
            This is for the first pass. For some reason, when the page loads
            it goes through this function. data['Screen[]'] isn't defined as
            data is empty.
        """
        screen = data['Screen[]']
        print(screen+"\n")
    except:
        """
            If this is the first pass, then exit the function
        """
        return render(request,'products/xps-webpage.html')
    

    return render(request,'products/xps-webpage.html')

def latitude(request):
    # This handles the AJAX POST from xps-webpage.html

    data = dict(request.POST)

    try:
        """
            This is for the first pass. For some reason, when the page loads
            it goes through this function. data['Screen[]'] isn't defined as
            data is empty.
        """
        screen = data['Screen[]']
        print(screen+"\n")

    except:
        """
            If this is the first pass, then exit the function
        """
        return render(request,'products/latitude-webpage.html')
    

    return render(request,'products/latitude-webpage.html')


def inspiron(request):
    # This handles the AJAX POST from xps-webpage.html

    data = dict(request.POST)

    try:
        """
            This is for the first pass. For some reason, when the page loads
            it goes through this function. data['Screen[]'] isn't defined as
            data is empty.
        """
        screen = data['Screen[]']
        print(screen+"\n")

    except:
        """
            If this is the first pass, then exit the function
        """
        return render(request,'products/inspiron-webpage.html')
    

    return render(request,'products/inspiron-webpage.html')


def alienware(request):
    # This handles the AJAX POST from xps-webpage.html

    data = dict(request.POST)

    try:
        """
            This is for the first pass. For some reason, when the page loads
            it goes through this function. data['Screen[]'] isn't defined as
            data is empty.
        """
        screen = data['Screen[]']
        print(screen+"\n")

    except:
        """
            If this is the first pass, then exit the function
        """
        return render(request,'products/alienware-webpage.html')
    

    return render(request,'products/alienware-webpage.html')

